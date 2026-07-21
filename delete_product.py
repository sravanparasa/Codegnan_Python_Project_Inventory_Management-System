from data import products

def delete_product():

    print("\n========== DELETE PRODUCT ==========")

    pid = input("Enter Product ID : ")

    for product in products:

        if product[0] == pid:

            print("\nProduct Details")
            print("-----------------------------")
            print("ID       :", product[0])
            print("Name     :", product[1])
            print("Category :", product[2])
            print("Price    :", product[3])
            print("Quantity :", product[4])

            choice = input("\nAre you sure you want to delete? (Y/N): ")

            if choice.upper() == "Y":
                products.remove(product)
                print("\nProduct Deleted Successfully!")
            else:
                print("\nDelete Operation Cancelled!")

            return

    print("\nProduct Not Found!")
