from login import login
from add_product import add_product
from view_products import view_products
from search_product import search_product
from update_product import update_product
from delete_product import delete_product
from purchase_stock import purchase_stock
from sell_product import sell_product
from reports import reports


while True:
    print("\n========== Inventory Management System ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Purchase Stock")
    print("7. Sell Product")
    print("8. Reports")
    print("9. Exit")

    try:
            choice = int(input("Enter Your Choice : "))

            if choice == 1:
                add_product()

            elif choice == 2:
                view_products()

            elif choice == 3:
                search_product()

            elif choice == 4:
                update_product()

            elif choice == 5:
                delete_product()

            elif choice == 6:
                purchase_stock()

            elif choice == 7:
                sell_product()

            elif choice == 8:
                reports()

            elif choice == 9:
                print("\nThank You for Using Inventory Management System!")
                break

            else:
                print("\nInvalid Choice!")

    except ValueError:
            print("\nPlease Enter Numbers Only!")
