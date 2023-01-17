import csv


with open("products2.csv", "r", encoding="utf-8") as product_file:
    file_writer = csv.DictReader(product_file, delimiter=";")
    for row in file_writer:
        name = row["Name"]
        old_price = int(row["Old price"])
        new_price = int(row["New price"])
        if old_price > new_price:
            print(name)
