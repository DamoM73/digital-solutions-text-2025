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
- [x] Python Skills
  - [x] Python Introduction
  - [x] PyQt
  - [x] Working with CSV
  - [x] Type Hints
  - [x] SQLite3
  - [x] SQLite3 - Reading
  - [x] SQLite3 - Creating
  - [x] SQLite3 - Updating and Deleting
  - [x] Populating Databases
  - [x] Working with JSON and XML
  - [x] Requests
  - [x] OurAPI
  - [x] Encryption
  - [x] Hashing
  - [x] Checksums
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
- [x] Activity Answers
- [x] Bibliography

## Outstanding content

- [x] Write the Checksums page in `content/07_python/`.
- [x] Add Python SQLite UPDATE and DELETE instruction, worked examples and activities. Added as `content/07_python/06_update_delete.md` after SQLite3 - Reading, using chinook.db.
- [ ] Write Utilities Introduction, Draw.io and Word Power-use in `content/09_tools/`; these are heading-only pages.
- [ ] Write Assessments Introduction, FIA1, FIA2, FIA3, IA1 and IA2 in `content/10_assessments/`; these are heading-only pages.
- [ ] Review the scope of `content/10_assessments/08_ia3.md`: its guidance refers to a specific healthcare dashboard stimulus, including practice manager, clinical staff and administration staff. Identify that task clearly or adapt the guidance for general use.
- [x] Complete `content/activity_answers.md` for the existing activities whose answer sections are empty: Data Security Management, Data Security Threats, relevant Documentation topics and the remaining Python topics (PyQt, Querying, Creating, Populating, JSON and XML, Requests and OurAPI). Working with CSV, Type Hints, Encryption, Hashing and Checksums are done. Match answers to actual activities; remove unused headings or identify open-ended tasks rather than imply an answer is supplied.
- [ ] Add solutions for activities introduced when the placeholder chapters are written.

## Corrections and consistency

- [x] Fix `content/08_sql/assets/CREATE/Activity_1e.sql`: removed the last line, `FOREIGN KEY("quantity") REFERENCES ""`, which referred to a table with no name.
- [x] Fill the empty Learning Goals in `content/07_python/07_creation.md` and `content/09_tools/03_figma.md`.
- [ ] Align the Home page's statement that every page starts with Learning Goals with the actual page structure. Either add goals consistently or qualify the statement in `content/index.md`.
- [x] Fix the normalisation link in `content/06_documentation/11_erd_rs.md`: `../04_data.md/03_structuring_data.md` should be `../04_data/03_structuring_data.md`.
- [x] Fix the JSON/XML activity link in `content/07_python/10_requests.md`: `./08_json.md` should be `./09_json.md`.
- [x] Add URL schemes to the 13 open-data links in `content/05_data_transmission/02_privacy.md` (the government portal list). Targets such as `data.gov.au` are currently interpreted as relative file paths.
- [x] Review the repeated `verify=False` examples in `content/07_python/10_requests.md`; make certificate verification the normal example and explain any classroom-specific certificate setup separately. Removed `verify=False` from all eight examples and added a caution explaining how to handle school-network SSL errors without turning off verification.
- [x] Finish the parameterised-query explanation in `content/07_python/06_queries.md`, where the paragraph ends at "Where we want to place a variable"; proofread the surrounding `sqlite3` explanation.
- [ ] Review the table-creation explanation in `content/07_python/07_creation.md`, distinguishing table creation from insertion order and foreign-key enforcement. Keep the prose, standalone SQL examples and Python example consistent about Driver, Seasons and Raced.
- [x] Correct "five basic features" in `content/10_assessments/08_ia3.md`; the following list contains six items.
- [x] Proofread headings and terminology, including "Existing Soultions" in `content/06_documentation/05_existing_solutions.md`, "EDR" in `content/06_documentation/11_erd_rs.md`, "Existing Soluitions" and "Psuedocode" in `content/activity_answers.md`, and DIWK/DIKW in `content/04_data/01_intro.md`.
- [x] Remove the empty trailing list item in the activities in `content/08_sql/03_where.md`.

## References and publication checks

- [x] Fix the Bibliography page. mystmd has no directive that lists a whole `.bib` file, so `content/bibliography.md` now cites every key in `references.bib` with `{cite:t}`, which produces the full References list. Corporate authors in `references.bib` are braced (for example `{{NBC News}}`) so they display in full.
- [ ] Convert bare citation keys in `content/04_data/01_intro.md`, including `nldigibeter_2019_problem` and `dataliteracy_2020_11`, to the project's working citation syntax. Neither key has an entry in `references.bib`, and the sources couldn't be verified; needs the title, author, year and URL of each source.
- [ ] Check assessment rules and response-limit claims against the applicable syllabus and school assessment instruments, especially `content/06_documentation/18_appendices.md` and the IA3 guidance. Record the source/version used.
- [ ] Inspect the rendered navigation, callouts, code blocks, citations, images and downloadable resources across all pages. A fresh HTML build with Jupyter Book 2.1.7 (mystmd 1.11.0) on 2 November 2026 built all 80 pages with no errors or warnings; only the Home, Python Introduction, Working with CSV, PyQt, Type Hints, Encryption, Hashing, Checksums and SQLite3 - Updating and Deleting pages have been inspected in a browser.
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

## Completed 3 November 2026

- Added a Unit Repositories section to `content/01_introduction/01_digital_solutions.md`, linking to the four unit repos with the syllabus unit titles and a reminder to fork each repo.
- Wrote the PyQt page (`content/07_python/02_pyqt.md`): a brief introduction to PyQt, with the PyQt-website logo (`content/07_python/assets/02/pyqt_logo.png`) linking to https://damom73.github.io/PyQt-website/.
- Wrote Type Hints (`content/07_python/04_type_hints.md`): basics, collections and checking with Pylance, with activity solutions in `content/07_python/assets/04/`.
- Renamed Ciphers to Encryption (`content/07_python/12_ciphers.md` replaced by `content/07_python/12_encryption.md`; `myst.yml` updated). Covers Caesar, Vigenère, Gronsfeld and one-time pad in Python, Fernet and RSA with the `cryptography` library, and storing keys safely. Activity solutions are in `content/07_python/assets/12/`.
- Wrote Hashing (`content/07_python/13_hashing.md`): `hashlib` and SHA-256, salted password hashing with `pbkdf2_hmac` (600,000 iterations) and `hmac.compare_digest`, and a SQLite login Datastore. Activity solutions are in `content/07_python/assets/13/`.
- Wrote Checksums (`content/07_python/14_checksums.md`): sum checksums, parity bits, the Luhn check digit, and CRC32 and SHA-256 file checksums. Activity solutions are in `content/07_python/assets/14/`.
- Wrote SQLite3 - Updating and Deleting (`content/07_python/06_update_delete.md`, after SQLite3 - Reading in `myst.yml`): parameterised UPDATE and DELETE on chinook.db, `commit()` and `rowcount`. Activity solutions are in `content/07_python/assets/06u/`.
- Completed Activity Solutions: added answers for User Insights, Use Case Diagrams, Success Criteria, Pseudocode, Data Flow Diagrams (new draw.io diagrams `content/assets/dfd_activity_2` and `_3`), ERDs and RS, Data Dictionaries, Data Connection Diagrams, Testing, Querying, Creating, Populating (Netflix), JSON and XML, Requests and OurAPI (Python answer files in `content/07_python/assets/06`–`11`). Removed the empty headings for pages with no activities (Managing and Manipulating Data, Data Security Management, Data Security Threats, Mind Maps, Existing Solutions, Mock-Ups, User Feedback, Evaluation Table, Impacts Table, PyQt). Requests answers were checked against simulated responses only, because JSONPlaceholder and httpbin couldn't be reached.
- Quick fixes: added Learning Goals to `07_python/07_creation.md` and `09_tools/03_figma.md`; fixed the normalisation link in `06_documentation/11_erd_rs.md` and the JSON/XML link in `07_python/10_requests.md`; added `https://` to the 13 open-data links in `05_data_transmission/02_privacy.md`. The "six basic features" correction, the proofreading fixes and the empty WHERE list item were already done in the repo.

## Review coverage

- All 80 table-of-contents entries have corresponding Markdown source files.
- Reviewed chapter structure, content presence, authoring gaps, activity-answer coverage, citation setup and local Markdown link/image targets across the source pages.
- Found 15 unresolved local link targets: two incorrect Markdown paths and 13 web addresses without URL schemes. No missing local image targets were found by that scan.
- Existing substantive chapters remain checked, with specific follow-up tasks above. No book content was changed as part of this checklist update.
- Code examples were inspected where relevant to the tasks above; they were not executed. No fresh build, remote-link validation or independent syllabus compliance audit was performed.
