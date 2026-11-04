# For Teachers

This page lists the external websites that students use while working through this text. Give this list to your school's IT team so they can whitelist these domains on the school firewall before the course starts.

:::{note} About this list
:class: dropdown
- The list covers the main domains only. Some installers and services load files from other domains behind the scenes. If something is still blocked after whitelisting, ask IT to check the firewall logs for the extra domains it needs.
- Some activities use the local address `127.0.0.1` (OurAPI runs on the student's own computer). This doesn't need whitelisting.
- `example.com`, `api.example.com` and `api.library.com` appear in code examples as placeholders. Students don't visit them.
- If your school network inspects HTTPS traffic, the Python `requests` activities may show SSL certificate errors. See the caution at the top of [](../07_python/10_requests.md).
:::

## Course websites

| Domain | Used for | Pages |
| --- | --- | --- |
| `damom73.github.io` | This text, the PyQt website and the Python refresher sites | All pages, [](../07_python/01_intro.md), [](../07_python/02_pyqt.md) |
| `github.com` | Student accounts, forking the unit repos, the OurAPI fork | [](01_digital_solutions.md), [](02_technologies_used.md), [](../07_python/11_ourapi.md) |

## Software and online tools

| Domain | Used for | Pages |
| --- | --- | --- |
| `www.python.org` | Python installer | [](02_technologies_used.md) |
| `apps.microsoft.com` | Python and mind mapping software from the Microsoft Store | [](02_technologies_used.md) |
| `apps.apple.com` | Mind mapping software from the Mac App Store | [](02_technologies_used.md) |
| `code.visualstudio.com` | VS Code installer | [](02_technologies_used.md) |
| `git-scm.com` | Git installer | [](02_technologies_used.md) |
| `desktop.github.com` | GitHub Desktop installer | [](02_technologies_used.md) |
| `sqlitebrowser.org` | DB Browser for SQLite installer | [](02_technologies_used.md) |
| `www.diagrams.net` | draw.io online diagram editor | [](02_technologies_used.md) |
| `get.diagrams.net` | draw.io desktop installer | [](02_technologies_used.md) |
| `www.figma.com` | Figma wireframes, mock-ups and prototypes | [](02_technologies_used.md) |
| `build-system.fman.io` | Qt Designer installer | [](02_technologies_used.md) |
| `sourceforge.net` | OurAPI download | [](../07_python/11_ourapi.md) |
| `www.mockaroo.com` | Generating sample data | [](../06_documentation/11_erd_rs.md) |

## Packages and extensions

| Domain | Used for | Pages |
| --- | --- | --- |
| `pypi.org` | Installing Python packages with `pip` (PyQt6, requests, cryptography) | [](02_technologies_used.md), [](../07_python/12_encryption.md) |
| `marketplace.visualstudio.com` | VS Code extensions | [](02_technologies_used.md), [](../02_coding/03_good_practice.md), [](../07_python/03_csv.md), [](../07_python/08_populate.md) |

## APIs used in code

| Domain | Used for | Pages |
| --- | --- | --- |
| `jsonplaceholder.typicode.com` | Practice API for GET, POST, PUT, PATCH and DELETE requests | [](../07_python/10_requests.md) |
| `httpbin.org` | Practice API for headers and timeouts | [](../07_python/10_requests.md) |
| `free-apis.github.io` | Directory of free APIs for extension activities | [](../07_python/10_requests.md) |

## Videos

| Domain | Used for | Pages |
| --- | --- | --- |
| `www.youtube.com` | Linked and embedded videos | Most chapters |
| `www.youtube-nocookie.com` | Embedded videos (privacy-enhanced YouTube) | Most chapters |

## Reading and reference sites

| Domain | Used for | Pages |
| --- | --- | --- |
| `www.w3schools.com` | Python and SQL reference | [](../02_coding/02_basic_features.md), all SQL Skills pages |
| `docs.python.org` | Python documentation | [](02_technologies_used.md) |
| `peps.python.org` | PEP 8 style guide | [](../02_coding/03_good_practice.md), [](../activity_answers.md) |
| `learnpython.com` | Python reading | [](../02_coding/02_basic_features.md) |
| `www.freecodecamp.org` | Data structures reading | [](../02_coding/02_basic_features.md) |
| `www.maketecheasier.com` | Windows PATH explanation | [](02_technologies_used.md) |
| `en.wikipedia.org` | Background reading | [](../04_data/02_data_principles.md), [](../05_data_transmission/05_security_threats.md) |
| `www.interaction-design.org` | Usability reading | [](../03_user_experience/02_usability_principles.md) |
| `www.tpgi.com` | Accessibility tools | [](../03_user_experience/02_usability_principles.md) |
| `www.lego.com` | Website analysed in the visual communication activities | [](../03_user_experience/03_visual_communication.md) |
| `help.figma.com` | Figma help | [](../09_tools/03_figma.md) |
| `www.tutorialspoint.com` | Data dictionary reading | [](../06_documentation/12_data_dictionaries.md) |
| `www.geeksforgeeks.org` | Security reading | [](../05_data_transmission/04_security_management.md) |
| `www.oaic.gov.au` | Australian Privacy Principles | [](../05_data_transmission/02_privacy.md), [](../05_data_transmission/04_security_management.md) |
| `haveibeenpwned.com` | Checking for data breaches | [](../05_data_transmission/02_privacy.md) |
| `privacy.net` | Privacy analyser | [](../05_data_transmission/02_privacy.md) |
| `www.security.org` | Data broker reading | [](../05_data_transmission/02_privacy.md) |
| `au.pcmag.com` | Data removal services reading | [](../05_data_transmission/02_privacy.md) |
| `www.abc.net.au` | News article | [](../05_data_transmission/02_privacy.md) |
| `abcnews.go.com` | News article | [](../05_data_transmission/05_security_threats.md) |
| `www.bbc.com` | News article | [](../05_data_transmission/05_security_threats.md) |
| `www.reuters.com` | News article | [](../05_data_transmission/05_security_threats.md) |
| `www.theguardian.com` | News article | [](../05_data_transmission/05_security_threats.md) |
| `www.wired.com` | News article | [](../05_data_transmission/05_security_threats.md) |
| `www.cpomagazine.com` | News article | [](../05_data_transmission/05_security_threats.md) |
| `money.cnn.com` | News article | [](../05_data_transmission/05_security_threats.md) |
| `www.breaches.cloud` | Data breach case studies | [](../05_data_transmission/05_security_threats.md) |

## Open data portals

These are used in the open data activities on the [](../05_data_transmission/02_privacy.md) page.

| Domain | Used for |
| --- | --- |
| `data.gov.au` | Australian Government open data |
| `abs.gov.au` | Australian Bureau of Statistics |
| `nationalmap.gov.au` | National Map |
| `data.qld.gov.au` | Queensland open data |
| `data.nsw.gov.au` | New South Wales open data |
| `data.vic.gov.au` | Victorian open data |
| `data.sa.gov.au` | South Australian open data |
| `data.wa.gov.au` | Western Australian open data |
| `data.act.gov.au` | ACT open data |
| `data.nt.gov.au` | Northern Territory open data |
| `thelist.tas.gov.au` | Tasmanian spatial data |
| `data.brisbane.qld.gov.au` | Brisbane City Council open data |
| `data-goldcoast.opendata.arcgis.com` | City of Gold Coast open data |
| `www.logan.qld.gov.au` | Logan City Council open data |
| `opendata.redland.qld.gov.au` | Redland City Council open data |
