import xml.etree.ElementTree as ET

xml_data = '''
<book>
    <title>1984</title>
    <author>George Orwell</author>
    <year>1949</year>
</book>
'''

root = ET.fromstring(xml_data)

print(f"Title: {root.find('title').text}")
print(f"Author: {root.find('author').text}")
print(f"Year: {root.find('year').text}")
