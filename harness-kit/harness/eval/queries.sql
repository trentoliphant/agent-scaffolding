-- Optional analysis queries over the ledger (DuckDB).
-- If you pre-register thresholds for a process experiment, commit them
-- before data collection begins (see the validation-plan pattern).
-- Run with DuckDB from harness/eval/:  duckdb -c ".read queries.sql"
-- (or paste individual queries). Ledger path is relative: ../ledger.jsonl
--
-- Convenience view over the ledger. Columns are declared explicitly so the
-- queries run on day zero, before any event of a given type exists
-- (read_json_auto would only infer columns already present in the data).
CREATE OR REPLACE VIEW ledger AS
SELECT * FROM read_json('../ledger.jsonl', format='newline_delimited',
  columns={ts:'VARCHAR', event:'VARCHAR', actor:'VARCHAR',
           session:'VARCHAR', party:'VARCHAR', task:'VARCHAR',
           state:'VARCHAR', note:'VARCHAR', "class":'VARCHAR',
           verdict:'VARCHAR', recommendation:'VARCHAR',
           self_verdict:'VARCHAR', self_confidence:'VARCHAR',
           verification:'VARCHAR[]', tasks:'VARCHAR[]',
           findings:'INTEGER', report:'VARCHAR', review:'VARCHAR',
           decision:'VARCHAR', level:'VARCHAR', human_gate:'BOOLEAN',
           issue:'VARCHAR', severity:'VARCHAR', status:'VARCHAR',
           route:'VARCHAR', target:'VARCHAR', phase:'VARCHAR',
           action:'VARCHAR', spec:'VARCHAR', mode:'VARCHAR',
           title:'VARCHAR'});

-- ---------------------------------------------------------------------
-- Q-C2a: Calibration table — implementer self-assessment vs reviewer
-- verdict, by task class.
-- PRE-REGISTERED THRESHOLDS (validation plan C2): a class is a pilot
-- candidate at n_tasks >= 8 AND calibration >= 0.90 AND zero
-- revise/escalate verdicts; a class with miscalibration >= 0.25 is a
-- standing reason to keep full gates.
-- ---------------------------------------------------------------------
WITH self AS (
  SELECT task, last(self_verdict ORDER BY ts) AS self_verdict,
         last(self_confidence ORDER BY ts) AS self_confidence
  FROM ledger
  WHERE event = 'task_state' AND state = 'agent_review'
        AND self_verdict IS NOT NULL
  GROUP BY task
), actual AS (
  SELECT task, last(verdict ORDER BY ts) AS verdict
  FROM ledger WHERE event = 'verdict' GROUP BY task
), cls AS (
  SELECT task, "class" FROM ledger WHERE event = 'task_created'
)
SELECT cls."class",
       count(*)                                            AS n_tasks,
       round(avg(CASE WHEN self.self_verdict = actual.verdict
                      THEN 1.0 ELSE 0.0 END), 2)           AS calibration,
       sum(CASE WHEN actual.verdict IN ('revise', 'escalate')
                THEN 1 ELSE 0 END)                         AS hard_misses
FROM actual
JOIN cls  USING (task)
LEFT JOIN self USING (task)
GROUP BY cls."class"
ORDER BY n_tasks DESC;

-- ---------------------------------------------------------------------
-- Q-C2b: Sensor participation — how many agent_review events carried a
-- self-assessment (mid-phase pulse check; a skipped sensor is data).
-- ---------------------------------------------------------------------
SELECT count(*)                                              AS reviews,
       sum(CASE WHEN self_verdict IS NOT NULL THEN 1 ELSE 0 END)
                                                             AS with_self
FROM ledger WHERE event = 'task_state' AND state = 'agent_review';

-- ---------------------------------------------------------------------
-- Q-C1: Assumption notes recorded at in_progress (cross-check against
-- review records for held/failed; failures are counted manually).
-- THRESHOLD: >=1 failed assumption causing rework, or >=2 orphaned
-- CANDIDATES.md entries, adopts the candidate layer.
-- ---------------------------------------------------------------------
SELECT ts, task, session, note
FROM ledger
WHERE event = 'task_state' AND state = 'in_progress'
      AND note ILIKE '%assumes:%'
ORDER BY ts;

-- ---------------------------------------------------------------------
-- Q-C3: Acting-party substitutions — any event where party deviates from
-- the default expectation (machine for agent roles, human for approver).
-- ---------------------------------------------------------------------
SELECT ts, event, actor, party, session, task
FROM ledger
WHERE party IS NOT NULL
      AND ((actor = 'approver' AND party != 'human')
           OR (actor != 'approver' AND party != 'machine'))
ORDER BY ts;

-- ---------------------------------------------------------------------
-- Q-C4: Named-verification A/B — audit findings rate for tasks with vs
-- without named verification contracts.
-- THRESHOLD: across >=6 tasks, boilerplate-review findings rarer (or
-- auditor reports engagement easier) in the named half -> adopt.
-- ---------------------------------------------------------------------
WITH named AS (
  SELECT task,
         (verification IS NOT NULL AND len(verification) > 0) AS has_named
  FROM ledger WHERE event = 'task_created'
), audited AS (
  SELECT unnest(tasks) AS task, findings
  FROM ledger WHERE event = 'audit'
)
SELECT named.has_named,
       count(DISTINCT named.task)        AS n_tasks,
       coalesce(sum(audited.findings), 0) AS total_audit_findings
FROM named LEFT JOIN audited USING (task)
GROUP BY named.has_named;

-- ---------------------------------------------------------------------
-- Q-GATE: Human Review Signal distribution + accumulation pressure over
-- the phase (context for the C2 pilot decision).
-- ---------------------------------------------------------------------
SELECT recommendation, count(*) AS n
FROM ledger WHERE event = 'verdict'
GROUP BY recommendation ORDER BY n DESC;
