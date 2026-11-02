import csv

with open("data/student_data.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    count = 0
    for row in csv_reader:
        print(f"{row[1]} {row[2]}: {row[3]}")
        count += 1
        if count == 5:
            break
