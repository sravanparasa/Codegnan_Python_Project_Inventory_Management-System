from data import products

def update_product():

    print("\n========== UPDATE PRODUCT ==========")

    pid = input("Enter Product ID : ")

    for product in products:

        if product[0] == pid:

            print("\nCurrent Details")
            print("-----------------------------")
            print("Name      :", product[1])
            print("Category  :", product[2])
            print("Price     :", product[3])
            print("Quantity  :", product[4])

            print("\nWhat do you want to update?")
            print("1. Price")
            print("2. Quantity")
            print("3. Both")

            choice = int(input("Enter Choice : "))

            try:

                if choice == 1:
                    product[3] = int(input("Enter New Price : "))
                    print("\nPrice Updated Successfully!")

                elif choice == 2:
                    product[4] = int(input("Enter New Quantity : "))
                    print("\nQuantity Updated Successfully!")

                elif choice == 3:
                    product[3] = int(input("Enter New Price : "))
                    product[4] = int(input("Enter New Quantity : "))
                    print("\nProduct Updated Successfully!")

                else:
                    print("\nInvalid Choice!")

            except ValueError:
                print("\nInvalid Input!")

            return

    print("\nProduct Not Found!")
