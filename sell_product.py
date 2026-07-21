from data import products, sales

def sell_product():

    print("\n========== SELL PRODUCT ==========")

    pid = input("Enter Product ID : ")

    for product in products:

        if product[0] == pid:

            print("\nAvailable Stock :", product[4])

            try:
                qty = int(input("Enter Selling Quantity : "))

                if qty <= 0:
                    print("Quantity must be greater than 0!")
                    return

                if qty > product[4]:
                    print("Insufficient Stock!")
                    return

                product[4] = product[4] - qty

                sales.append([product[0], product[1], qty])

                print("\nProduct Sold Successfully!")
                print("Remaining Stock :", product[4])

            except ValueError:
                print("Invalid Quantity!")

            return

    print("\nProduct Not Found!")
