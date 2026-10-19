# Expense Tracker with Budget Advice

expensesList = []   # list of expenses, each one is a dictionary
budget = {}         # category -> monthly budget
categories = ["Food", "Travel", "Shopping", "Books", "Entertainment", "Other"]


def get_number(message):
    """Keep asking until the user types a valid positive number."""
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("Amount cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


def choose_category():
    """Show the category list and return the chosen one."""
    print("Categories:")
    for i, name in enumerate(categories, start=1):
        print(f"  {i}. {name}")
    while True:
        try:
            pick = int(input("Choose a category number: "))
            if 1 <= pick <= len(categories):
                return categories[pick - 1]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")


def totals_by_category():
    totals = {}
    for e in expensesList:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals


def show_advice():
    """The decision step: compare spending with budget and give advice."""
    totals = totals_by_category()
    if not totals:
        print("No expenses added yet.")
        return
    print("\n===== SUMMARY & ADVICE =====")
    for category, spent in totals.items():
        limit = budget.get(category)
        if limit is None:
            print(f"{category}: Rs {spent} spent (no budget set)")
            continue
        percent = spent / limit * 100
        if percent > 100:
            print(f"{category}: Rs {spent} / Rs {limit} -> {round(percent - 100)}% OVER budget. Consider reducing spending here.")
        elif percent > 80:
            print(f"{category}: Rs {spent} / Rs {limit} -> {round(percent)}% used. Be careful.")
        else:
            print(f"{category}: Rs {spent} / Rs {limit} -> on track ({round(percent)}% used).")


print("Welcome to Expense Tracker")

while True:
    print("\n====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Set Budget")
    print("5. Summary & Advice")
    print("6. Exit")

    try:
        choice = int(input("Please Enter Your Choice : "))
    except ValueError:
        print("Please enter a number between 1 and 6.")
        continue

    # 1. ADD EXPENSE
    if choice == 1:
        date = input("Enter the date of the expense (DD-MM-YYYY): ")
        category = choose_category()
        description = input("Enter a short description: ")
        amount = get_number("Enter the amount: ")

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }
        expensesList.append(expense)
        print("Expense added successfully.")

    # 2. VIEW ALL EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("No expenses added yet.")
        else:
            print("===== All Expenses =====")
            count = 1
            for e in expensesList:
                print(f"Expense {count} -> {e['date']}, {e['category']}, {e['description']}, Rs {e['amount']}")
                count = count + 1

    # 3. TOTAL
    elif choice == 3:
        total = 0
        for e in expensesList:
            total = total + e["amount"]
        print("TOTAL EXPENSES = Rs", total)

    # 4. SET BUDGET
    elif choice == 4:
        category = choose_category()
        budget[category] = get_number(f"Enter monthly budget for {category} (Rs): ")
        print(f"Budget set for {category}.")

    # 5. SUMMARY & ADVICE
    elif choice == 5:
        show_advice()

    # 6. EXIT
    elif choice == 6:
        print("Thank you for using Expense Tracker.")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")
