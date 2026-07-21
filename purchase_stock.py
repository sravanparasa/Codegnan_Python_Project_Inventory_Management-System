from data import products, purchases

def purchase_stock():

    print("\n========== PURCHASE STOCK ==========")

    pid = input("Enter Product ID : ")

    for product in products:

        if product[0] == pid:

            print("\nCurrent Stock :", product[4])

            try:
                qty = int(input("Enter Purchased Quantity : "))

                if qty <= 0:
                    print("Quantity must be greater than 0!")
                    return

                product[4] = product[4] + qty

                purchases.append([product[0], product[1], qty])

                print("\nStock Purchased Successfully!")
                print("Updated Stock :", product[4])

            except ValueError:
                print("Invalid Quantity!")

            return

    print("\nProduct Not Found!")
