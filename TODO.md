# To Do

Reviewed against all 80 pages in `myst.yml` on 2 November 2026. Checked items indicate that substantive page content exists; they do not imply that every example, external resource or assessment claim has been validated. Outstanding corrections are listed separately below.

## Chapter content

- [x] Home
- [x] Introduction
  - [x] Digital Solutions
  - [x] Technologies
- [x] Coding
  - [x] Coding Introduction  
  - [x] Basic Features
  - [x] Good Practice
  - [x] Programming Paradigms
- [x] User Experience
  - [x] User Experience Introduction
  - [x] Usability
  - [x] Visual Communication
  - [x] Impacts
- [x] Data
  - [x] Data Introduction
  - [x] Data Principles
  - [x] Structuring Data
  - [x] Managing and Manipulating Data
- [x] Data Transmission
  - [x] Data Transmission Introduction
  - [x] Data Privacy
  - [x] Networks
  - [x] Data Security Management
  - [x] Data Security - Threats
- [x] Documentation
  - [x] Documentation Introduction
  - [x] Mind Maps
  - [x] User Insights
  - [x] Use Case Diagrams
  - [x] Existing Solutions
  - [x] Success Criteria
  - [x] Mock-ups
  - [x] Pseudocode
  - [x] Desk Checking
  - [x] Data Flow Diagrams
  - [x] ERD and RS
  - [x] Data Dictionaries
  - [x] Data Connection Diagrams
  - [x] Testing
  - [x] User Feedback
  - [x] Evaluation Table
  - [x] Impacts Table
  - [x] Appendices
- [ ] Python Skills
  - [x] Python Introduction
  - [ ] PyQt
  - [x] Working with CSV
  - [ ] Type Hints
  - [x] SQLite3
  - [x] SQLite3 - Reading
  - [x] SQLite3 - Creating
  - [ ] SQLite3 - Updating and Deleting (not covered by the existing creation page)
  - [x] Populating Databases
  - [x] Working with JSON and XML
  - [x] Requests
  - [x] OurAPI
  - [ ] Ciphers
  - [ ] Hashing
  - [ ] Checksums
- [x] SQL Skills
  - [x] SQL Introduction
  - [x] SELECT  
  - [x] WHERE  
  - [x] Filters and Aggregators
  - [x] ORDER BY  
  - [x] GROUP BY and HAVING  
  - [x] Subqueries
  - [x] JOIN  
  - [x] CREATE TABLE
  - [x] INSERT  
  - [x] UPDATE  
  - [x] DELETE  
- [ ] Utilities Skills
  - [ ] Utilities Introduction
  - [x] DB Browser
  - [x] Figma
  - [ ] Draw.io
  - [ ] Word
- [ ] Assessments
  - [ ] Assessments Introduction
  - [ ] FIA1 - Technical Proposal
  - [ ] FIA2 - Digital Solution
  - [ ] FIA3 - Digital Solution
  - [x] FIAE - Exam
  - [ ] IA1 - Technical Proposal
  - [ ] IA2 - Digital Solution
  - [x] IA3 - Digital Solution
  - [x] EA - Exam
- [ ] Activity Answers (partially populated; see follow-up tasks below)
- [ ] Bibliography (page contains a bibliography directive; rendering and citation integration still need verification)

## Outstanding content

- [ ] Write the PyQt, Type Hints, Ciphers, Hashing and Checksums pages in `content/07_python/`. These currently contain only headings.
- [ ] Add Python SQLite UPDATE and DELETE instruction, worked examples and activities. `content/07_python/07_creation.md` currently covers CREATE only; add any new pages to `myst.yml`.
- [ ] Write Utilities Introduction, Draw.io and Word Power-use in `content/09_tools/`; these are heading-only pages.
- [ ] Write Assessments Introduction, FIA1, FIA2, FIA3, IA1 and IA2 in `content/10_assessments/`; these are heading-only pages.
- [ ] Review the scope of `content/10_assessments/08_ia3.md`: its guidance refers to a specific healthcare dashboard stimulus, including practice manager, clinical staff and administration staff. Identify that task clearly or adapt the guidance for general use.
- [ ] Complete `content/activity_answers.md` for the existing activities whose answer sections are empty: Data Security Management, Data Security Threats, relevant Documentation topics and the listed Python topics (Working with CSV is done). Match answers to actual activities; remove unused headings or identify open-ended tasks rather than imply an answer is supplied.
- [ ] Add solutions for activities introduced when the placeholder chapters are written.

## Corrections and consistency

- [ ] Fill the empty Learning Goals in `content/07_python/07_creation.md` and `content/09_tools/03_figma.md`.
- [ ] Align the Home page's statement that every page starts with Learning Goals with the actual page structure. Either add goals consistently or qualify the statement in `content/index.md`.
- [ ] Fix the normalisation link in `content/06_documentation/11_erd_rs.md`: `../04_data.md/03_structuring_data.md` should be `../04_data/03_structuring_data.md`.
- [ ] Fix the JSON/XML activity link in `content/07_python/10_requests.md`: `./08_json.md` should be `./09_json.md`.
- [ ] Add URL schemes to the 13 open-data links in `content/05_data_transmission/02_privacy.md` (the government portal list). Targets such as `data.gov.au` are currently interpreted as relative file paths.
- [ ] Review the repeated `verify=False` examples in `content/07_python/10_requests.md`; make certificate verification the normal example and explain any classroom-specific certificate setup separately.
- [ ] Finish the parameterised-query explanation in `content/07_python/06_queries.md`, where the paragraph ends at "Where we want to place a variable"; proofread the surrounding `sqlite3` explanation.
- [ ] Review the table-creation explanation in `content/07_python/07_creation.md`, distinguishing table creation from insertion order and foreign-key enforcement. Keep the prose, standalone SQL examples and Python example consistent about Driver, Seasons and Raced.
- [ ] Correct "five basic features" in `content/10_assessments/08_ia3.md`; the following list contains six items.
- [ ] Proofread headings and terminology, including "Existing Soultions" in `content/06_documentation/05_existing_solutions.md`, "EDR" in `content/06_documentation/11_erd_rs.md`, "Existing Soluitions" and "Psuedocode" in `content/activity_answers.md`, and DIWK/DIKW in `content/04_data/01_intro.md`.
- [ ] Remove the empty trailing list item in the activities in `content/08_sql/03_where.md`.

## References and publication checks

- [ ] Fix the Bibliography page. In the 2 November 2026 build, inline `{cite}` citations resolve and show their references on each page, but `content/bibliography.md` renders empty: the `{bibliography}` directive lists no entries. The bibliography configuration in `myst.yml` is still commented out.
- [ ] Convert bare citation keys in `content/04_data/01_intro.md`, including `nldigibeter_2019_problem` and `dataliteracy_2020_11`, to the project's working citation syntax.
- [ ] Check assessment rules and response-limit claims against the applicable syllabus and school assessment instruments, especially `content/06_documentation/18_appendices.md` and the IA3 guidance. Record the source/version used.
- [ ] Inspect the rendered navigation, callouts, code blocks, citations, images and downloadable resources across all pages. A fresh HTML build with Jupyter Book 2.1.7 (mystmd 1.11.0) on 2 November 2026 built all 80 pages with no errors or warnings; only the Home, Python Introduction and Working with CSV pages have been inspected in a browser.
- [ ] Check external links, embedded videos and practice-question downloads for availability and usefulness. This review checked local file targets; it did not test remote resources or inspect the contents of linked PDF/DOCX files.

## Completed 2 November 2026

- Wrote the Home page welcome content (`content/index.md`).
- Wrote the Python Introduction (`content/07_python/01_intro.md`).
- Wrote Working with CSV (`content/07_python/03_csv.md`) using `data/student_data.csv`, with activity solutions in `content/07_python/assets/03/` included in `content/activity_answers.md`.
- Updated `requirements.txt` to `jupyter-book>=2.1.7,<3`.
- Escaped `$` in the Clearview AI entry in `references.bib` so the file parses.
- Added the missing `ulhaq_2018_the` and `interactiondesignfoundation_2014_what` entries to `references.bib`. Their years come from the citation keys and need confirming.
- Set the language to `text` for the six pseudocode blocks in `content/06_documentation/09_desk_checking.md`.
- Added explicit `(naming-conventions)=` and `(f1-database-structure)=` labels in `content/02_coding/03_good_practice.md` and `content/07_python/08_populate.md`.

## Review coverage

- All 80 table-of-contents entries have corresponding Markdown source files.
- Reviewed chapter structure, content presence, authoring gaps, activity-answer coverage, citation setup and local Markdown link/image targets across the source pages.
- Found 15 unresolved local link targets: two incorrect Markdown paths and 13 web addresses without URL schemes. No missing local image targets were found by that scan.
- Existing substantive chapters remain checked, with specific follow-up tasks above. No book content was changed as part of this checklist update.
- Code examples were inspected where relevant to the tasks above; they were not executed. No fresh build, remote-link validation or independent syllabus compliance audit was performed.
