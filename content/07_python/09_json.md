# Working with JSON and XML

:::{dropdown} Learning Goals
By the end of this section you will:
- understand how to convert JSON strings and files into Python dictionaries
- understand how to convert Python dictionaries into JSON strings and files
- understand how to extract data from an XML string and file using Python
- understand how to save Python data to an XML file
:::

## JSON

**JSON** (JavaScript Object Notation) is a lightweight data format used to store and exchange data. It’s easy for humans to read and write, and easy for machines to parse and generate.

A JSON object is similar to a Python dictionary.

:::{code} json
{
  "name": "Alice",
  "age": 25,
  "is_student": true,
  "courses": ["Math", "Science"]
}
:::

### Python and JSON

Python provides a built-in module called `json` to work with JSON data.

**JSON to Python**

Convert a JSON-formatted string into a Python dictionary.

:::{hint} What is a JSON-formatted string?
:class: dropdown
A **JSON-formatted string** is a text-based way to represent structured data using the **JavaScript Object Notation (JSON)** format. It uses **key–value pairs** and **arrays** to organize data, and it is commonly used for data exchange between systems, especially in web applications.

**JSON Rules:**

- Keys and string values must be in **double quotes** (`"`).
- Values can be:

  - Strings (`"text"`)
  - Numbers (`123`)
  - Booleans (`true`, `false`)
  - `null`
  - Arrays (`[ ]`)
  - Nested objects (`{ }`)
:::

:::{code} python
import json

json_string = '{"name": "Alice", "age": 25}'
python_dict = json.loads(json_string)
print(python_dict)
print(python_dict['name'])
:::

**Python to JSON**

Convert a Python dictionary into a JSON-formatted string.

:::{code} python
import json

data = {'name': 'Bob', 'age': 30, 'is_student': False}
json_string = json.dumps(data)
print(json_string)
:::

### Working with JSON Files

**Reading from a JSON file**

Open a JSON file, reads its JSON content, then convert it into a Python object, depending on the JSON file format:

- key&ndash;value pair &rarr; dictionary
- array &rarr; list

:::{code} python
import json

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
:::

**Writing to a JSON file**

Convert a Python dictionary into a JSON-formatted string and write it to a JSON file.

:::{code} python
import json

data = {'name': 'Carol', 'age': 28}
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)
:::

:::{hint} Advanced Tips
:class: dropdown
- Use `indent=4` to pretty-print JSON when writing.
- Use `sort_keys=True` to alphabetically sort dictionary keys in output.
- Use `json.loads(json_string)` for strings and `json.load(file)` for files.
:::

### Summary

| Task             | Method         |
| ---------------- | -------------- |
| JSON String &nbsp;&rarr;&nbsp; Python Object | `json.loads()` |
| Python Object &nbsp;&rarr;&nbsp; JSON String | `json.dumps()` |
| JSON File &nbsp;&rarr;&nbsp; Python Object  | `json.load()`  |
| Python Object &nbsp;&rarr;&nbsp; JSON File   | `json.dump()`  |

:::{seealso} JSON Activities
:class: dropdown
**Activity 1: Decode a JSON String**

You are given a JSON string that represents a book in a digital library. Convert it to a Python dictionary and print each piece of information.

JSON String:

```python
json_data = '{"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "available": true}'
```

Instructions:

1. Import the `json` module.
2. Convert the `json_data` string to a Python dictionary using `json.loads()`.
3. Print out the book title, author, year, and availability status in a readable format.

Expected Output:

```
Title: The Hobbit  
Author: J.R.R. Tolkien  
Year: 1937  
Available: True
```

---

**Activity 2: Read a JSON List of Students**

You receive JSON data representing a list of students. Convert it into a Python list of dictionaries and print the name and grade for each student.

JSON String:

```python
students_json = '''
[
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Carol", "grade": 95}
]
'''
```

Instructions:

1. Import the `json` module.
2. Use `json.loads()` to convert `students_json` into a Python list.
3. Loop through each student and print their name and grade.

Expected Output:

```
Alice: 90  
Bob: 85  
Carol: 95
```

---

**Activity 3: Read a Single Object from a JSON File**

You are given a file named [car.json](./assets/09/car.json) that contains information about a vehicle. Your job is to load the file into Python and display the data.

Instructions:

1. Use Python to open and read `car.json`.
2. Convert the JSON file into a Python dictionary using `json.load()`.
3. Print out each property in the following format:

Expected Output:

```
Make: Toyota  
Model: Corolla  
Year: 2020  
Electric: False
```

---

**Activity 4: Read a List of Objects from a JSON File**

You are given a file called [inventory.json](./assets/09/inventory.json) which contains a list of items in a school store. Convert the data to a Python list and display the stock level for each item.

Instructions:

1. Open and read the `inventory.json` file in Python.
2. Convert the JSON data to a Python list of dictionaries.
3. Loop through the list and print each item with its stock level:

Expected Output:

```
Pencil: 120  
Notebook: 60  
Eraser: 35
```

---

**Activity 5: Convert a Python Dictionary to a JSON String**

You are building a simple digital contact book. Start with a Python dictionary and convert it to a JSON string so it can be stored or sent over a network.

Instructions:

1. Create a Python dictionary with the following details:

```python
contact = {
    "name": "Liam",
    "phone": "0455 123 456",
    "email": "liam@example.com",
    "subscribed": True
}
```

2. Use `json.dumps()` to convert the dictionary into a JSON-formatted string.
3. Print the resulting JSON string.
4. Add `indent=4` to make the output easier to read.

Expected Output (formatted):

```json
{
    "name": "Liam",
    "phone": "0455 123 456",
    "email": "liam@example.com",
    "subscribed": true
}
```

---

**Activity 6: Save Python Data to a JSON File**

You are creating a list of movies for a media app. Convert the data from Python to JSON and save it to a file called `movies.json`.

Instructions:

1. Create the following Python list of dictionaries:

```python
movies = [
    {"title": "Inception", "year": 2010},
    {"title": "The Matrix", "year": 1999},
    {"title": "Interstellar", "year": 2014}
]
```

2. Use `json.dump()` to save this data to a file named `movies.json`.
3. Include `indent=2` when saving to make the JSON file readable.

Expected Result (`movies.json` file):

```json
[
  {
    "title": "Inception",
    "year": 2010
  },
  {
    "title": "The Matrix",
    "year": 1999
  },
  {
    "title": "Interstellar",
    "year": 2014
  }
]
```
:::

---

## XML

**XML** (eXtensible Markup Language) is a markup language used to store and transport data. It’s similar to HTML but focuses on describing data rather than displaying it.

**Example XML:**

:::{code} XML
<student>
    <name>Alice</name>
    <age>25</age>
    <courses>
        <course>Math</course>
        <course>Science</course>
    </courses>
</student>
:::

### Python and XML

Python includes a built-in module called `xml.etree.ElementTree` (often shortened to `ET`) for parsing and creating XML data.

**Parsing XML from a String**

This code parses an XML string into a **Python XML element**.

:::{hint} What is an XML Element?
:class: dropdown
A Python **XML element** is an **object**—specifically, an instance of the `xml.etree.ElementTree.Element` class. It behaves like an object with methods (e.g., `.find()`, `.text`, `.attrib`) that allow you to navigate and manipulate XML data.
:::

:::{code} python
import xml.etree.ElementTree as ET

xml_data = """
<student>
    <name>Alice</name>
    <age>25</age>
</student>
"""

root = ET.fromstring(xml_data)
print(root.tag)  # Output: student
print(root.find('name').text)  # Output: Alice
print(root.find('age').text)   # Output: 25
:::

**Parsing XML from a File**

Create an XML element from a string and access its child elements.

student.xml:

:::{code} XML
<student>
    <name>Bob</name>
    <age>22</age>
</student>
:::

Python code:

:::{code} python
tree = ET.parse('student.xml')
root = tree.getroot()

print(root.find('name').text)  # Output: Bob
print(root.find('age').text)   # Output: 22
:::

**Looping Through Elements**

Parse an XML string containing multiple students, then loops through each `<student>` element to print their name and age in a formatted sentence.


:::{code} python
xml_data = """
<students>
    <student>
        <name>Alice</name>
        <age>25</age>
    </student>
    <student>
        <name>Bob</name>
        <age>22</age>
    </student>
</students>
"""

root = ET.fromstring(xml_data)

for student in root.findall('student'):
    name = student.find('name').text
    age = student.find('age').text
    print(f"{name} is {age} years old")
:::

**Creating an XML Document**

:::{code} python
import xml.etree.ElementTree as ET

root = ET.Element("student")
name = ET.SubElement(root, "name")
name.text = "Carol"
age = ET.SubElement(root, "age")
age.text = "23"

tree = ET.ElementTree(root)
tree.write("new_student.xml", encoding="utf-8", xml_declaration=True)
:::

### Summary

| Task              | Method                      |
| ----------------- | --------------------------- |
| Parse from string | `ET.fromstring(xml_string)` |
| Parse from file   | `ET.parse(file)`            |
| Find element      | `element.find('tag')`       |
| Find all elements | `element.findall('tag')`    |
| Get element text  | `element.text`              |
| Write to XML file | `tree.write('file.xml')`    |

:::{seealso} XML Activities
:class: dropdown
**Activity 1: Parse an XML String into Python**

You are given a string containing XML data about a book. Convert it to Python using `ElementTree`, and print the values of each tag.

XML Data (as a string):

```python
xml_data = '''
<book>
    <title>1984</title>
    <author>George Orwell</author>
    <year>1949</year>
</book>
'''
```

Instructions:

1. Import `xml.etree.ElementTree as ET`.
2. Use `ET.fromstring(xml_data)` to parse the XML into a Python object.
3. Print the title, author, and year from the XML.

Expected Output:

```
Title: 1984  
Author: George Orwell  
Year: 1949
```

---

**Activity 2: Read XML from a File and Loop Through Elements**

You are working with an XML file named [students.xml](./assets/09/students.xml) that contains multiple student records. Load the file and display each student's name and age.

Instructions:

1. Use `ET.parse('students.xml')` and get the root with `.getroot()`.
2. Loop through each `<student>` element.
3. Print the name and age of each student.

Expected Output:

```
Alice is 25 years old  
Bob is 22 years old
```

---

**Activity 3: Convert a Python Dictionary to an XML Element**

You have a dictionary with information about a movie. Convert it to an XML structure and print it.

Python Dictionary:

```python
movie = {
    "title": "The Matrix",
    "director": "The Wachowskis",
    "year": "1999"
}
```

Instructions:

1. Import `xml.etree.ElementTree as ET`.
2. Create a root element called `<movie>`.
3. Add child elements for `title`, `director`, and `year`, using the values from the dictionary.
4. Print the resulting XML string using `ET.tostring()`.

Expected Output (formatted):

```xml
<movie>
    <title>The Matrix</title>
    <director>The Wachowskis</director>
    <year>1999</year>
</movie>
```

---

**Activity 4: Create an XML File from a List of Dictionaries**

You are given a Python list of people. Convert it into XML and save it to a file called `people.xml`.

Python List:

```python
people = [
    {"name": "Alice", "age": "30"},
    {"name": "Bob", "age": "25"}
]
```

Instructions:

1. Create a root element called `<people>`.
2. For each person in the list, create a `<person>` sub-element with `<name>` and `<age>` inside.
3. Use `ET.ElementTree()` to write the XML to `people.xml`.

**Expected Output (`people.xml`):**

```xml
<people>
    <person>
        <name>Alice</name>
        <age>30</age>
    </person>
    <person>
        <name>Bob</name>
        <age>25</age>
    </person>
</people>
```
:::