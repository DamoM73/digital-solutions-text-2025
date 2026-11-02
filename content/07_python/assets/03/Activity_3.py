import csv

search_id = int(input("Enter a student ID: "))
found = False

with open("data/student_data.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for record in csv_reader:
        if int(record["student_id"]) == search_id:
            print(f"Name: {record['first_name']} {record['last_name']}")
            print(f"Email: {record['email']}")
            found = True
            break

if not found:
    print("Student not found")
