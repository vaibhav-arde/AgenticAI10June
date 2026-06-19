# Expense Tracker

expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully.")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nExpenses:")
            for expense in expenses:
                print(
                    f"{expense['category']} - ₹{expense['amount']}"
                )

    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total Expenses: ₹{total}")

        if total > 5000:
            print("Warning: High spending!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")