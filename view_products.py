from data import products

def view_products():

    print("\n======================= PRODUCT LIST ==========================\n")

    if len(products) == 0:
        print("No Products Available!")
        return

    print("{:<12}{:<20}{:<18}{:<12}{:<10}".format(
        "ID", "NAME", "CATEGORY", "PRICE", "QTY"))
    print("-" * 72)

    for product in products:
        print("{:<12}{:<20}{:<18}{:<12}{:<10}".format(
            product[0],
            product[1],
            product[2],
            product[3],
            product[4]
        ))
