import xml.etree.ElementTree as ET

people = [
    {"name": "Alice", "age": "30"},
    {"name": "Bob", "age": "25"}
]

root = ET.Element("people")

for person in people:
    person_element = ET.SubElement(root, "person")
    name = ET.SubElement(person_element, "name")
    name.text = person["name"]
    age = ET.SubElement(person_element, "age")
    age.text = person["age"]

tree = ET.ElementTree(root)
ET.indent(tree)
tree.write("people.xml", encoding="utf-8")
