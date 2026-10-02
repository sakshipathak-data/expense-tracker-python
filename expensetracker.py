#Personal Expense Tracker (CLI)

categories = ("Food", "Travel", "Shopping", "Bills", "Other")  
expenses = []  
 
name = input("Enter your name: ").strip().title()

while True:
    budget_text = input("Enter monthly budget: ")
    try:
        budget = float(budget_text)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if budget <= 0:
        print("Budget must be greater than 0.")
        continue
    break

print(f"\nWelcome, {name}! Budget: ₹{budget:.2f}")

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search by Category")
    print("4. Delete an Expense")
    print("5. Summary Report")
    print("6. Exit")
    choice = input("Choose: ").strip()

    # ---------- 3. Add Expense ----------
    if choice == "1":
        desc = input("Description: ").strip().title()
        if desc == "":
            print("Description cannot be empty.")
            continue

        while True:
            amount_text = input("Amount: ")
            try:
                amount = float(amount_text)
            except ValueError:
                print("Please enter a valid number.")
                continue
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break

        while True:
            category = input("Category (Food/Travel/Shopping/Bills/Other): ").strip().title()
            if category in categories:
                break
            print("Invalid category. Try again.")

        expense = {"desc": desc, "amount": amount, "category": category}
        expenses.append(expense)
        print("Expense added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            print("\n--- All Expenses ---")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['desc']} | ₹{exp['amount']:.2f} | {exp['category']}")

    elif choice == "3":
        search = input("Enter category to search: ").strip().lower()
        found_total = 0
        found_count = 0

        print(f"\n--- Expenses in '{search.title()}' ---")
        for exp in expenses:
            if exp["category"].lower() == search:
                found_count += 1
                found_total += exp["amount"]
                print(f"{found_count}. {exp['desc']} | ₹{exp['amount']:.2f}")

        if found_count == 0:
            print("No expenses found in this category.")
        else:
            print(f"Total for {search.title()}: ₹{found_total:.2f}")

    # ---------- 6. Delete an Expense ----------
    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses to delete.")
            continue

        print("\n--- All Expenses ---")
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp['desc']} | ₹{exp['amount']:.2f} | {exp['category']}")

        num_text = input("Enter the number to delete: ").strip()
        if not num_text.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        num = int(num_text)
        if num < 1 or num > len(expenses):
            print("Invalid number. Out of range.")
        else:
            removed = expenses.pop(num - 1)
            print(f"Deleted: {removed['desc']} (₹{removed['amount']:.2f})")

    
    elif choice == "5":
        if len(expenses) == 0:
            print("No expenses yet. Nothing to summarize.")
            continue

        total = 0
        highest = expenses[0]
        lowest = expenses[0]
        category_totals = {}      
        used_categories = set()   

        for exp in expenses:
            total += exp["amount"]
            if exp["amount"] > highest["amount"]:
                highest = exp
            if exp["amount"] < lowest["amount"]:
                lowest = exp
            cat = exp["category"]
            category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]
            used_categories.add(cat)

        average = total / len(expenses)
        remaining = budget - total

        print("\n===== Summary Report =====")
        print(f"Total spent : ₹{total:.2f}")
        print(f"Average     : ₹{average:.2f}")
        print(f"Highest     : {highest['desc']} (₹{highest['amount']:.2f})")
        print(f"Lowest      : {lowest['desc']} (₹{lowest['amount']:.2f})")

        print("\nCategory-wise total:")
        for cat, cat_total in category_totals.items():
            print(f"  {cat:<10} ₹{cat_total:.2f}")

        print("\nCategories used:", ", ".join(sorted(used_categories)))

        if remaining >= 0:
            print(f"\nBudget remaining: ₹{remaining:.2f}")
        else:
            print(f"\n⚠ Budget exceeded by ₹{abs(remaining):.2f}")

        percent = (total / budget) * 100
        if percent < 50:
            level = "Good"
        elif percent <= 90:
            level = "Careful"
        else:
            level = "Danger"
        print(f"Spending level: {level} ({percent:.1f}% of budget used)")

    elif choice == "6":
        print(f"Goodbye, {name}! Happy saving.")
        break

    else:
        print("Invalid option. Please choose between 1 and 6.")