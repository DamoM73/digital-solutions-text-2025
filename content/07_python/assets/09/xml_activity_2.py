import xml.etree.ElementTree as ET

tree = ET.parse("students.xml")
root = tree.getroot()

for student in root.findall("student"):
    name = student.find("name").text
    age = student.find("age").text
    print(f"{name} is {age} years old")
