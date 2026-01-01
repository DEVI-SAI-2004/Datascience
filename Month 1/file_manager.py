import csv
import os
import shutil
from datetime import datetime
def backup_data(source='data/expenses.csv', backup_dir='data/backups/'):
    """Creates a timestamped backup of the current expense data."""
    try:
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{backup_dir}backup_{timestamp}.csv"
        
        shutil.copy(source, backup_path)
        print(f"✅ Backup created: {backup_path}")
    except FileNotFoundError:
        print("❌ Error: No data found to backup.")
    except Exception as e:
        print(f"❌ Backup failed: {e}")
def save_expense_to_file(expense, filename='data/expenses.csv'):
    """Appends a single expense object to the CSV file."""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as file:
        fieldnames = ['amount', 'category', 'date', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header only if file is new
        if not file_exists:
            writer.writeheader()
            
        writer.writerow(expense.to_dict())

def load_expenses_from_file(filename='data/expenses.csv'):
    """Reads the CSV and returns a list of data dictionaries."""
    if not os.path.exists(filename):
        return []
        
    expenses = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return expenses