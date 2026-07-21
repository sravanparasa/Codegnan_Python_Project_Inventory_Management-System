from data import products

def search_product():

    print("\n========== SEARCH PRODUCT ==========")

    pid = input("Enter Product ID : ")

    found = False

    for product in products:
        if product[0] == pid:
            print("\nProduct Found")
            print("-" * 40)
            print("Product ID   :", product[0])
            print("Product Name :", product[1])
            print("Category     :", product[2])
            print("Price        :", product[3])
            print("Quantity     :", product[4])
            print("-" * 40)
            found = True
            break

    if found == False:
        print("\nProduct Not Found!")
