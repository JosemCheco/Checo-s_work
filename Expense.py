expenses = []

def add_expense():
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter expense amount: "))
        expenses.append((description, amount))
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please enter a valid number.")

def display_expenses():
    print("\nList of Expenses:")
    for index, (description, amount) in enumerate(expenses, start=1):
        print(f"{index}. Description: {description}, Amount: {amount}")

def calculate_expense ():
    total = sum(amount for _, amount in expenses)
    print(f"\nTotal Expenses: {total}")

def main():
    while True:
        print("\n1. Add Expense\n2. Display Expenses\n3. Calculate Total Expenses\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            calculate_expense.()
        elif choice == "4":
            print("Closing")
            break
        else:
            print("Choose a valid option.")

main()
