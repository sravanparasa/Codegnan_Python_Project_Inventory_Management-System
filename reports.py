from data import products, purchases, sales

def reports():

    print("\n========== INVENTORY REPORT ==========")

    print("Total Products             :", len(products))
    print("Purchase Transactions      :", len(purchases))
    print("Sales Transactions         :", len(sales))

    low_stock = 0

    for product in products:
        if product[4] < 5:
            low_stock += 1

    print("Low Stock Products (<5)    :", low_stock)

    print("\n========== LOW STOCK PRODUCTS ==========")

    found = False

    for product in products:
        if product[4] < 5:
            print("----------------------------------------")
            print("ID       :", product[0])
            print("Name     :", product[1])
            print("Category :", product[2])
            print("Price    :", product[3])
            print("Quantity :", product[4])
            found = True

    if found == False:
        print("No Low Stock Products!")

    print("----------------------------------------")
