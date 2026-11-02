# Working with CSV

:::{dropdown} Learning Goals
By the end of this section you will:
- understand how to read a CSV file as lists using `csv.reader`
- understand how to read a CSV file as dictionaries using `csv.DictReader`
- understand how to write data to a CSV file using `csv.writer` and `csv.DictWriter`
- understand how to read and write TSV files and other delimiters
:::

:::{note} Resources needed
:class: dropdown
- **student_data.csv** from our course repo, which is in the **data** folder. Our Python files go in the main repo folder, so our code opens the file as `data/student_data.csv`. The files we create on this page are also saved in the **data** folder.
- The [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) VS Code extension makes CSV files much easier to read.
:::

## CSV files

Remember from [Networks](../05_data_transmission/03_networking.md) that a **CSV** (Comma-Separated Values) file stores tabular data as plain text. Each line is a row, and each value in the row is separated by a comma. The first row is usually a **header row** that names each column.

Here are the first few lines of **student_data.csv**:

:::{code} text
student_id,first_name,last_name,email,gender
1,Benji,Dungee,bdungee0@icq.com,Male
2,Rufe,Spridgeon,rspridgeon1@bandcamp.com,Male
3,Fallon,Tomovic,ftomovic2@xing.com,Female
:::

The file has 400 students, and each student has five fields: `student_id`, `first_name`, `last_name`, `email` and `gender`.

### Python and CSV

We could read a CSV file line by line and split each line at the commas ourselves, but that breaks as soon as a value contains a comma. Instead, Python provides a built-in module called `csv` that handles these problems for us.

:::{hint} Why not just use split(",")?
:class: dropdown
Consider a value such as `Dungee, Benji`. If we used `line.split(",")`, the name would be broken into two separate values. The `csv` module knows that a value wrapped in double quotes (`"Dungee, Benji"`) is a single value, even though it contains a comma.
:::

## Reading CSV files

### Reading rows as lists

`csv.reader` reads a CSV file one row at a time. Each row is returned as a **list** of values.

:::{code} python
:linenos:
import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    print(header)

    for row in csv_reader:
        print(row)
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; imports Python's built-in `csv` module
- **line 3** &rarr; opens **student_data.csv** from the **data** folder in read mode (`"r"`) and stores the open file in `csv_file`
  - `with` closes the file for us when the block finishes
  - `encoding="utf-8"` makes sure special characters are read correctly
- **line 4** &rarr; creates a reader object that will give us one row at a time
- **line 5** &rarr; `next()` takes the first row (the header row) from the reader, so it isn't processed with the data
- **line 6** &rarr; prints the header row
- **line 8** &rarr; loops through every remaining row in the file
- **line 9** &rarr; prints each row as a list
:::

The output starts and ends like this:

:::{code} text
['student_id', 'first_name', 'last_name', 'email', 'gender']
['1', 'Benji', 'Dungee', 'bdungee0@icq.com', 'Male']
['2', 'Rufe', 'Spridgeon', 'rspridgeon1@bandcamp.com', 'Male']
['3', 'Fallon', 'Tomovic', 'ftomovic2@xing.com', 'Female']
...
['399', 'Giselbert', 'Jenoure', 'gjenoureb2@house.gov', 'Agender']
['400', 'Di', 'Andrick', 'dandrickb3@skype.com', 'Female']
:::

### Everything is a string

Look closely at the output above. The `student_id` values are `'1'`, `'2'` and `'3'`, not `1`, `2` and `3`. A CSV file is just text, so **every value read from a CSV file is a string**. If we need a number, we have to convert it ourselves.

:::{code} python
:linenos:
import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
        student_id = int(row[0])
        if student_id > 395:
            print(f"{student_id}: {row[1]} {row[2]}")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 5** &rarr; skips the header row. We don't need to keep it, so we don't store it in a variable
- **line 8** &rarr; `row[0]` is the first value in the row (`student_id`), and `int()` converts it from a string to an integer
- **line 9** &rarr; compares the student ID as a number. If we tried `row[0] > 395` instead, Python would raise a `TypeError` because we can't compare a string with an integer
- **line 10** &rarr; uses the index of each value to print the ID, first name and last name
:::

Output:

:::{code} text
396: Wini Alforde
397: Laverne Ferrillo
398: Cyrill Bohike
399: Giselbert Jenoure
400: Di Andrick
:::

### Reading rows as dictionaries

Using indexes like `row[1]` and `row[2]` works, but it's hard to remember which number matches which column. `csv.DictReader` solves this by reading each row as a **dictionary**. It uses the header row as the keys, so we can access each value by its column name.

:::{code} python
:linenos:
import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for record in csv_reader:
        if record["last_name"].startswith("O'"):
            print(f"{record['first_name']} {record['last_name']}: {record['email']}")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 4** &rarr; creates a `DictReader` object. It reads the header row automatically, so we don't need `next()`
- **line 6** &rarr; loops through each row, with each `record` being a dictionary such as `{'student_id': '1', 'first_name': 'Benji', 'last_name': 'Dungee', ...}`
- **line 7** &rarr; checks if the student's last name starts with `O'`
- **line 8** &rarr; prints the student's name and email, using the column names as keys
:::

Output:

:::{code} text
Alys O'Donnelly: aodonnelly1p@goodreads.com
Salmon O'Doherty: sodoherty1y@archive.org
Leanor O'Brogane: lobrogane2q@gnu.org
Thoma O' Loughran: toloughran5f@elpais.com
Una O'Dee: uodee7w@last.fm
Martino O'Cannan: mocannanar@elpais.com
:::

:::{tip} Summary
:class: dropdown
- `csv.reader` &rarr; each row is a list, accessed by index (`row[1]`)
- `csv.DictReader` &rarr; each row is a dictionary, accessed by column name (`record["first_name"]`)
- Every value read from a CSV file is a string, so we convert numbers with `int()` or `float()`

`DictReader` makes our code easier to read and keeps working even if the order of the columns changes, so it is usually the better choice.
:::

## Writing CSV files

### Writing rows from lists

`csv.writer` writes lists to a CSV file, one list per row.

:::{code} python
:linenos:
import csv

new_students = [
    ["student_id", "first_name", "last_name"],
    [401, "Aroha", "Ngata"],
    [402, "Liam", "Nguyen"],
    [403, "Priya", "Sharma"],
]

with open("data/new_students.csv", mode="w", encoding="utf-8", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(new_students)
:::

:::{important} Explanation of Code
:class: dropdown
- **lines 3&ndash;8** &rarr; creates a list of lists. The first list is the header row and each other list is one student
- **line 10** &rarr; opens **new_students.csv** in write mode (`"w"`). If the file doesn't exist it is created, and if it does exist it is overwritten
  - `newline=""` lets the `csv` module control the line endings
- **line 11** &rarr; creates a writer object for the open file
- **line 12** &rarr; `writerows()` writes every list in `new_students` as a row. To write one row at a time we would use `writerow()` instead
:::

**new_students.csv**:

:::{code} text
student_id,first_name,last_name
401,Aroha,Ngata
402,Liam,Nguyen
403,Priya,Sharma
:::

Notice that the numbers didn't need to be converted to strings. `csv.writer` converts every value to text as it writes it.

:::{danger} Always use newline="" when writing
:class: dropdown
If we leave out `newline=""` when opening a file to write a CSV, Windows adds an extra blank line between every row. Always include `newline=""` when writing CSV files, so our code works the same way on Windows and macOS.
:::

### Writing rows from dictionaries

`csv.DictWriter` writes dictionaries to a CSV file. We tell it the column names with `fieldnames`, and it puts each value in the right column.

The code below reads **student_data.csv** and creates a new file called **student_names.csv**. The new file has the student ID and the student's full name written as `last_name, first_name`.

:::{code} python
:linenos:
import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as in_file:
    csv_reader = csv.DictReader(in_file)

    with open("data/student_names.csv", mode="w", encoding="utf-8", newline="") as out_file:
        fieldnames = ["student_id", "full_name"]
        csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for record in csv_reader:
            full_name = f"{record['last_name']}, {record['first_name']}"
            csv_writer.writerow({"student_id": record["student_id"], "full_name": full_name})
:::

:::{important} Explanation of Code
:class: dropdown
- **line 3** &rarr; opens **student_data.csv** to read from
- **line 6** &rarr; opens **student_names.csv** to write to. Both files are open at the same time
- **line 7** &rarr; lists the column names for the new file, in the order they will appear
- **line 8** &rarr; creates a `DictWriter` object that uses those column names
- **line 9** &rarr; `writeheader()` writes the header row using the `fieldnames`
- **line 11** &rarr; loops through each student in **student_data.csv**
- **line 12** &rarr; joins the last name and first name, separated by a comma and a space
- **line 13** &rarr; writes one row. The keys of the dictionary must match the `fieldnames`
:::

**student_names.csv** starts like this:

:::{code} text
student_id,full_name
1,"Dungee, Benji"
2,"Spridgeon, Rufe"
3,"Tomovic, Fallon"
:::

### Quoting

Look at the `full_name` values in **student_names.csv**. Each name contains a comma, so `DictWriter` has wrapped the value in double quotes. This is called **quoting**. It tells any program reading the file that `"Dungee, Benji"` is one value, not two.

When we read the file back with the `csv` module, the quotes are removed and the name stays together:

:::{code} python
:linenos:
import csv

with open("data/student_names.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    first_row = next(csv_reader)
    print(first_row)
:::

Output:

:::{code} text
['1', 'Dungee, Benji']
:::

By default, the `csv` module only quotes values that need it, such as values that contain the delimiter, a double quote or a new line. This is why we don't need to worry about it ourselves.

## TSV files and other delimiters

The character that separates values is called the **delimiter**. CSV files use a comma, but other files use different delimiters. The most common is the **TSV** (Tab-Separated Values) file, which uses a tab character (`"\t"`).

The `csv` module works with any delimiter. We just add `delimiter=` when we create the reader or writer.

### Writing a TSV file

The code below converts **student_data.csv** into a TSV file called **student_data.tsv**.

:::{code} python
:linenos:
import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as in_file:
    csv_reader = csv.reader(in_file)

    with open("data/student_data.tsv", mode="w", encoding="utf-8", newline="") as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        tsv_writer.writerows(csv_reader)
:::

:::{important} Explanation of Code
:class: dropdown
- **line 4** &rarr; reads **student_data.csv** with the default comma delimiter
- **line 6** &rarr; opens **student_data.tsv** to write to
- **line 7** &rarr; creates a writer that separates values with a tab instead of a comma
- **line 8** &rarr; writes every row from the reader straight into the TSV file
:::

**student_data.tsv** starts like this (the gaps are tabs):

:::{code} text
student_id	first_name	last_name	email	gender
1	Benji	Dungee	bdungee0@icq.com	Male
2	Rufe	Spridgeon	rspridgeon1@bandcamp.com	Male
:::

### Reading a TSV file

To read the TSV file, we use the same `delimiter="\t"` with our reader. This works with both `csv.reader` and `csv.DictReader`.

:::{code} python
:linenos:
import csv

with open("data/student_data.tsv", mode="r", encoding="utf-8") as tsv_file:
    tsv_reader = csv.DictReader(tsv_file, delimiter="\t")

    for record in tsv_reader:
        if record["student_id"] == "100":
            print(record)
:::

:::{important} Explanation of Code
:class: dropdown
- **line 4** &rarr; creates a `DictReader` that splits each row at the tabs
- **line 7** &rarr; finds the student with the ID `"100"`. We compare with the string `"100"` because every value read from the file is a string
- **line 8** &rarr; prints the whole dictionary for that student
:::

Output:

:::{code} text
{'student_id': '100', 'first_name': 'Hasty', 'last_name': 'Muller', 'email': 'hmuller2r@dmoz.org', 'gender': 'Male'}
:::

:::{caution} Using the wrong delimiter
:class: dropdown
If we read a TSV file without `delimiter="\t"`, Python looks for commas. It doesn't find any, so each whole line is read as a single value. If our data looks like one long value per row, the first thing to check is the delimiter.
:::

## Summary

| Task | Method |
| --- | --- |
| Read rows as lists | `csv.reader(file)` |
| Read rows as dictionaries | `csv.DictReader(file)` |
| Skip the header row (`csv.reader`) | `next(reader)` |
| Write one row from a list | `writer.writerow(list)` |
| Write many rows from lists | `writer.writerows(list_of_lists)` |
| Write rows from dictionaries | `csv.DictWriter(file, fieldnames=...)` |
| Write the header row (`DictWriter`) | `writer.writeheader()` |
| Use a different delimiter | `delimiter="\t"` |
| Open a file for writing | `open(..., mode="w", newline="")` |

:::{seealso} CSV Activities
:class: dropdown
All activities use **student_data.csv** from our course repo.

**Activity 1: Read the first five students**

Use `csv.reader` to print the full name and email of the first five students in **student_data.csv**.

Instructions:

1. Import the `csv` module and open **student_data.csv**.
2. Use `csv.reader` to read the file and skip the header row.
3. Print the first name, last name and email of the first five students, then stop.

Expected Output:

```text
Benji Dungee: bdungee0@icq.com
Rufe Spridgeon: rspridgeon1@bandcamp.com
Fallon Tomovic: ftomovic2@xing.com
Olly Rooze: orooze3@google.com.br
Andreana Reoch: areoch4@squidoo.com
```

---

**Activity 2: Count the .edu email addresses**

Use `csv.DictReader` to count how many students have an email address ending in `.edu`.

Instructions:

1. Open **student_data.csv** with `csv.DictReader`.
2. Loop through each student and check if their email ends with `.edu`.
3. Print the total.

Expected Output:

```text
27 students have a .edu email address
```

---

**Activity 3: Find a student by ID**

Ask the user for a student ID and print that student's name and email.

Instructions:

1. Ask the user to enter a student ID and convert it to an integer.
2. Use `csv.DictReader` to search **student_data.csv** for that ID. Remember that `record["student_id"]` is a string.
3. If the student is found, print their name and email. If not, print `Student not found`.

Expected Output (when the user enters `250`):

```text
Enter a student ID: 250
Name: Jeri Bottomer
Email: jbottomer6x@hc360.com
```

Expected Output (when the user enters `999`):

```text
Enter a student ID: 999
Student not found
```

---

**Activity 4: Save the .edu students to a new file**

Create a new file called **edu_students.csv** that only contains the students with a `.edu` email address.

Instructions:

1. Read **student_data.csv** with `csv.DictReader`.
2. Use `csv.DictWriter` to write to **edu_students.csv** with the columns `student_id`, `first_name`, `last_name` and `email` (leave out `gender`).
3. Write the header row, then write a row for each student with a `.edu` email address.

Expected Result (first four lines of **edu_students.csv**):

```text
student_id,first_name,last_name,email
35,Darcee,Pauls,dpaulsy@wisc.edu
75,Bernete,Laise,blaise22@illinois.edu
76,Coletta,Mation,cmation23@columbia.edu
```

The finished file should have 28 lines: the header row and 27 students.

---

**Activity 5: Create a TSV email list**

Create a TSV file called **student_emails.tsv** that contains only the student ID and email for every student.

Instructions:

1. Read **student_data.csv** with `csv.DictReader`.
2. Use `csv.writer` with `delimiter="\t"` to write to **student_emails.tsv**.
3. Write a header row of `student_id` and `email`, then a row for each student.

Expected Result (first four lines of **student_emails.tsv**, the gaps are tabs):

```text
student_id	email
1	bdungee0@icq.com
2	rspridgeon1@bandcamp.com
3	ftomovic2@xing.com
```

---

**Activity 6: Read the TSV email list**

Read the **student_emails.tsv** file we created in Activity 5 and print every student whose email address ends in `.gov`.

Instructions:

1. Open **student_emails.tsv** with `csv.DictReader` and the correct delimiter.
2. Print the student ID and email of each student with a `.gov` email address.

Expected Output (first five of 18 lines):

```text
55: sswainson1i@usda.gov
59: gburleton1m@cdc.gov
95: smordin2m@va.gov
106: eclendening2x@irs.gov
114: acresswell35@fema.gov
```
:::
