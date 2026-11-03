import json

students_json = '''
[
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85},
    {"name": "Carol", "grade": 95}
]
'''

students = json.loads(students_json)

for student in students:
    print(f"{student['name']}: {student['grade']}")
