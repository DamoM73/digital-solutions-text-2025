import csv

edu_count = 0

with open("data/student_data.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for record in csv_reader:
        if record["email"].endswith(".edu"):
            edu_count += 1

print(f"{edu_count} students have a .edu email address")
