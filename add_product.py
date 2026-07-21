from data import products

def add_product():

    print("\n========== ADD PRODUCT ==========")

    pid = input("Enter Product ID : ")

    for product in products:
        if product[0] == pid:
            print("Product ID already exists!")
            return

    pname = input("Enter Product Name : ")
    category = input("Enter Category : ")
    price = int(input("Enter Price : "))
    quantity = int(input("Enter Quantity : "))

    products.append([pid, pname, category, price, quantity])

    print("\nProduct Added Successfully!")
