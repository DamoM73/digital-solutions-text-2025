# Populating Databases

:::{dropdown} In this section you will...
- Learn to read data from a csv file into a SQLite database
:::

:::{note} You will need...
:class: dropdown
- [Digital Solutions Unit 3 repository](https://github.com/DamoM73/DS-2025-Unit-3)
- [CSV to Table Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=phplasma.csv-to-table)
- [SQLite Visual Studio Code Extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
:::

In this section we will learn how to parse a csv file into a SQLite database. We will populate the `f1_driver.db` with the data contained in the `F1Drivers_Dataset.csv` file. We will continue to use the MVC architecture, meaning this code will be placed in the `Datastore` class and be called from the `main.py` file.


