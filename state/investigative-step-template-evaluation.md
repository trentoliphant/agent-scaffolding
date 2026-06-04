# Investigative Step Template Evaluation

This note records an evaluation of whether the repository now needs an
optional investigative-step template note or variant.

It is a working evaluation note, not a durable decision by itself.

## Question

After the guide-layer extraction from `research_model/`, should the repository
also add an optional investigative-step template note or variant?

## Materials Compared

- `templates/core/step_spec.template.md`
- `docs/guide/domain-implementation-extensions.md`
- `state/research-model-extraction-review.md`
- `docs/examples/research-to-design/README.md`

## Evaluation

At the moment, an optional investigative-step template note is not clearly
justified.

The current baseline already has:

- a portable step template with sections for objective, dependencies, inputs,
  outputs, verification, trace, and deferred questions
- guide-layer language for research-heavy domains covering evidence
  discipline, explicit open-question tracking, and exploratory plan mutation
- a promoted example showing a research-to-design pattern in practice

That means the main missing ideas from `research_model/` are now represented
without adding more template complexity.

## Why A Template Addition Is Not Yet Justified

- the current `step_spec` template is deliberately portable across domains
- adding investigative-only sections now would make the baseline heavier for
  builders who do not need them
- the strongest research-specific prompts can already be expressed inside the
  current sections:
  - questions to answer can live in `Objective`, `Scope`, or `Questions Deferred`
  - methodology can live in `Execution Details`
  - evidence expectations can live in `Trace Requirements` and `Validation Requirements`
  - rabbit-hole limits can live in `Out of Scope` and `Execution Notes`
- the guide now explains when those concerns should be made explicit for
  research-heavy domains

## What Would Change This Judgment

An investigative-step template note or variant would make more sense if:

- builders repeatedly struggle to represent methodology and evidence
  expectations inside the current step template
- multiple current examples start using the same investigative-step structure
- a real project adopting the scaffold asks for a reusable investigative-step
  appendix rather than more guide text

## Recommendation

Do not change `templates/core/step_spec.template.md` yet.

Prefer to:

1. keep the current portable baseline template
2. rely on guide-layer instruction for research-heavy domains
3. watch for repeated builder pressure before adding an investigative-step
   appendix or variant
