accounts = []


def addAccount():
    account_no = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")
    account_type = input("Enter Account Type (Savings/Current): ")
    balance = float(input("Enter Opening Balance: "))
    city = input("Enter City: ")

    account = {
        "No": account_no,
        "Name": name,
        "Type": account_type,
        "Balance": balance,
        "City": city
    }

    accounts.append(account)

    print("Account added successfully.")


def displayAccounts():
    if len(accounts) == 0:
        print("No accounts available.")
        return

    print("\n----------------------------------------------------------")
    print("Account No\tName\t\tType\t\tBalance\t\tCity")
    print("----------------------------------------------------------")

    for account in accounts:
        print(account["No"], "\t\t",
              account["Name"], "\t\t",
              account["Type"], "\t",
              account["Balance"], "\t\t",
              account["City"])


def searchAccount():
    value = input("Enter Account Number or Account Holder Name: ")

    found = False

    for account in accounts:
        if (str(account["No"]) == value or
                account["Name"].lower() == value.lower()):

            print("\nAccount Found")
            print("----------------------------")
            print("Account No :", account["No"])
            print("Name       :", account["Name"])
            print("Type       :", account["Type"])
            print("Balance    :", account["Balance"])
            print("City       :", account["City"])

            found = True

    if found == False:
        print("Account not found.")


def updateAccount():
    account_no = int(input("Enter Account Number to update: "))

    found = False

    for account in accounts:

        if account["No"] == account_no:

            found = True

            print("\n1. Change Account Holder Name")
            print("2. Change Account Type")
            print("3. Change Balance")
            print("4. Change City")

            choice = input("Enter your choice: ")

            if choice == "1":
                account["Name"] = input("Enter new name: ")

            elif choice == "2":
                account["Type"] = input("Enter new account type: ")

            elif choice == "3":
                account["Balance"] = float(input("Enter new balance: "))

            elif choice == "4":
                account["City"] = input("Enter new city: ")

            else:
                print("Invalid choice.")
                return

            print("Account updated successfully.")
            break

    if found == False:
        print("Account Number not found.")


def deleteAccount():
    account_no = int(input("Enter Account Number to delete: "))

    found = False

    for account in accounts:

        if account["No"] == account_no:

            accounts.remove(account)

            found = True

            print("Account deleted successfully.")
            break

    if found == False:
        print("Account Number not found.")


def sortAccounts():

    if len(accounts) == 0:
        print("No accounts available for sorting.")
        return

    print("\n1. Sort by Account Holder Name")
    print("2. Sort by Balance")
    print("3. Sort by City")

    choice = input("Enter your choice: ")

    if choice == "1":
        accounts.sort(key=lambda x: x["Name"].lower())

    elif choice == "2":
        accounts.sort(key=lambda x: x["Balance"])

    elif choice == "3":
        accounts.sort(key=lambda x: x["City"].lower())

    else:
        print("Invalid choice.")
        return

    print("Accounts sorted successfully.")

    displayAccounts()