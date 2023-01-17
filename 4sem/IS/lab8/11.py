import csv


key = ""
products = {}


def add_product():
    name = input("Enter name of the product: ")
    price = input("Enter price of the product: ")
    quantity = input("Enter quantity of the product: ")
    products[name] = {
        "price": price,
        "quantity": quantity
    }


def view_product():
    name = input("Enter name of the product: ")
    if name in products:
        print("\tname: " + name)
        print("\tprice: " + products[name]["price"])
        print("\tquantity: " + products[name]["quantity"])
    else:
        print("There is no such product in stock")


def rewrite_product():
    name = input("Enter name of the product: ")
    if name in products:
        price = input("Enter price of the product: ")
        quantity = input("Enter quantity of the product: ")
        products[name] = {
            "price": price,
            "quantity": quantity
        }
    else:
        print("There is no such product in stock")


def delete_product():
    name = input("Enter name of the product: ")
    if name in products:
        del products[name]


def save_products():
    names = ["Name", "Price", "Quantity"]
    with open("products.csv", "w", encoding="utf-8") as product_file:
        file_writer = csv.DictWriter(
            product_file, delimiter=";", lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for product in products:
            file_writer.writerow(
                {"Name": product, "Price": products[product]["price"], "Quantity": products[product]["quantity"]})


def download_products():
    with open("products.csv", "r", encoding="utf-8") as product_file:
        file_writer = csv.DictReader(product_file, delimiter=";")
        for row in file_writer:
            name = row["Name"]
            price = row["Price"]
            quantity = row["Quantity"]
            products[name] = {
                "price": price,
                "quantity": quantity
            }
    for product in products:
        print("Name: " + product)
        print("Price: " + products[product]["price"])
        print("Quantity: " + products[product]["quantity"], end="\n\n")


while(key != "7"):
    print(
        "--------------------------------------\n"
        "1. Add product\n"
        "2. View product\n"
        "3. Rewrite product\n"
        "4. Delete product\n"
        "5. Save products in csv file\n"
        "6. Download products from csv file\n"
        "7. Exit\n"
        "--------------------------------------"
    )

    key = input()
    if key == "1":
        add_product()
    elif key == "2":
        view_product()
    elif key == "3":
        rewrite_product()
    elif key == "4":
        delete_product()
    elif key == "5":
        save_products()
    elif key == "6":
        download_products()
