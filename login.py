def login():

    while True:

        print("\n========== LOGIN ==========")

        username = input("Enter Username : ")
        password = input("Enter Password : ")

        if username == "admin" and password == "1234":
            print("\nLogin Successful!")
            break
        else:
            print("\nInvalid Username or Password! Try Again.\n")
