import csv


school = input("School: ")
class_ = input("Class: ")
persons = []


with open("rez.csv", "r", encoding="utf-8") as rez_file:
    file_writer = csv.DictReader(rez_file, delimiter=",")
    for row in file_writer:
        login = row["login"]
        row_school = login[12:14]
        row_class = login[15:17]
        if row_school == school and row_class == class_:
            row_name = row["user_name"]
            name = row_name[8:-2]
            score = row["Score"]
            persons.append((name, score))

persons = sorted(persons, key=lambda person: person[0], reverse=True)
persons = sorted(persons, key=lambda person: -int(person[1]))
for person in persons:
    print(*person)
