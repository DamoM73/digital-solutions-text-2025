# Evaluation Table

The evaluation table is the core document for demonstrating your evaluation of the solution. It connects your success criteria directly to evidence from testing and user feedback, then uses that evidence to justify refinements you made and recommendations for future improvement.

## Purpose

The ISMG requires you to:

- evaluate features and components (user experience and programmed components) against your success criteria
- make refinements and recommendations that are explicitly justified by testing outcomes and user feedback

A well-constructed evaluation table provides a clear, structured record of both.

## Structure

Each row corresponds to one success criterion from your criteria table. The columns move logically from the criterion code, through the evidence, to the judgment, and finally to action.

| Criterion | Evidence | Status | Judgment | Refinement / Recommendation |
| --- | --- | --- | --- | --- |
| SC1 | | | | |
| SC2 | | | | |

### Column guide

**Criterion** — use the criterion code from your criteria table (e.g. `SC1`, `SC2`). Do not restate the criterion here; the marker will cross-reference your criteria table. Using codes also allows you to reference specific criteria in annotations elsewhere in your response.

**Evidence** — describe specific, concrete evidence that relates to this criterion. This must come from one or more of:
- results from your testing table (e.g. a test that passed or failed)
- user feedback (e.g. a comment from a survey or observation session)
- your own observed system behaviour during testing

Avoid vague statements like "the app worked well". Reference specific test cases or feedback items by name or number.

**Status** — summarise the outcome of the criterion using one of three values:
- `Met` — the evidence shows the criterion was fully achieved
- `Partially Met` — the evidence shows the criterion was achieved in part but not fully
- `Not Met` — the evidence shows the criterion was not achieved

The status must be consistent with your judgment. It is a quick reference only — the judgment column carries the marks.

**Judgment** — make a direct judgment about whether and how well the criterion was met, based on your evidence. This is not a description — it is a reasoned conclusion. Connect the evidence explicitly to the criterion, for example: "SC1 was met because..." or "SC1 was only partially met, as testing revealed...".

**Refinement / Recommendation** — state what action was taken or should be taken as a result of your judgment. A *refinement* is a change you already made to the solution during development. A *recommendation* is a change you would make in a future iteration. Both must follow logically from the judgment.

## What makes a strong evaluation

The ISMG uses the qualifiers *critical*, *feasible*, and *superficial* to describe evaluation quality. The difference comes down to how tightly your judgment is connected to the criterion and the evidence.

| Qualifier | What it looks like |
| --- | --- |
| Critical | Judgment explicitly references the criterion; evidence is specific and directly supports the judgment; refinement or recommendation logically follows and targets the identified issue |
| Feasible | Judgment relates to the criterion but the connection to evidence is general; refinement or recommendation is present but not fully specific |
| Superficial | Criterion is described rather than evaluated; evidence is absent or vague; refinement or recommendation is missing or unconnected to the judgment |

## Example row

| Criterion | Evidence | Status | Judgment | Refinement / Recommendation |
| --- | --- | --- | --- | --- |
| SC1 | T04: 3/4 users navigated without assistance. Feedback Q2: back button not visible on settings screen. | Partially Met | SC1 partially met — navigation was intuitive for most users but the missing back button reduced effectiveness. | Refinement: back button added to settings screen; T04 re-run successfully. Recommendation: retest with a larger group to confirm fix across different screen sizes. |

*In this example, T04 refers to test case 4 from the testing table, and Feedback Q2 refers to question 2 from the user feedback survey.*