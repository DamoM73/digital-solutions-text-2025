import xml.etree.ElementTree as ET

movie = {
    "title": "The Matrix",
    "director": "The Wachowskis",
    "year": "1999"
}

root = ET.Element("movie")

for key, value in movie.items():
    child = ET.SubElement(root, key)
    child.text = value

ET.indent(root)
print(ET.tostring(root, encoding="unicode"))
