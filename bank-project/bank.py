import bankCrud as b1


while True:

    print("\n==========================================")
    print("          BANK ACCOUNT MANAGEMENT")
    print("==========================================")

    print("1. Add Account")
    print("2. Display Accounts")
    print("3. Update Account")
    print("4. Search Account")
    print("5. Delete Account")
    print("6. Sort Accounts")
    print("7. Exit")

    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        b1.addAccount()

    elif choice == "2":
        b1.displayAccounts()

    elif choice == "3":
        b1.updateAccount()

    elif choice == "4":
        b1.searchAccount()

    elif choice == "5":
        b1.deleteAccount()

    elif choice == "6":
        b1.sortAccounts()

    elif choice == "7":
        print("Thank you for using Bank Account Management.")
        break

    else:
        print("Please enter a valid choice.")