import os
from expense import Expense
from file_manager import save_expense_to_file
from file_manager import load_expenses_from_file
from reports import generate_basic_report, generate_category_report
import utils

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n" + "="*42)
    print("     💰 PERSONAL FINANCE MANAGER 💰")
    print("="*42)
    print("1. Add New Expense")
    print("2. View All Expenses (Brief)")
    print("3. Generate Reports (Coming Soon)")
    print("4. Exit")
    print("-" * 42)
    print("6. Backup Data")

def add_expense_flow():
    print("\n📝 ADD NEW EXPENSE")
    amount = utils.get_valid_float("Enter amount: ")
    
    print("Categories: Food, Transport, Entertainment, Shopping, Other")
    category = input("Enter category: ").capitalize()
    
    date = utils.get_valid_date("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    # Create Object (OOP Requirement)
    new_expense = Expense(amount, category, date, description)
    
    # Save to CSV (Persistence Requirement)
    save_expense_to_file(new_expense)
    print(f"\n✅ Expense added successfully: {new_expense}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense_flow()
        elif choice == '2':
            print("\n📋 Saved Expenses:")
            # In a real app, you'd load and print here
            print("Check data/expenses.csv for full records.")
        elif choice == '3':
            print("\n🔍 GENERATING REPORTS...")
            all_expenses = load_expenses_from_file() # Load data from CSV
            
            if all_expenses:
                generate_basic_report(all_expenses)
                generate_category_report(all_expenses)
            else:
                print("❌ No expenses found. Try adding some first!")
        elif choice == '4':
            print("👋 Goodbye! Stay on budget!")
            break
        else:
            print("❌ Invalid choice. Please select 1-4.")
        
        input("\nPress Enter to continue...")
        clear_screen()
        elif choice == '6':
            print("\n💾 INITIALIZING BACKUP...")
            backup_data()

if __name__ == "__main__":
    main()