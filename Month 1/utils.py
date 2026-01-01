from datetime import datetime

def get_valid_float(prompt):
    """Ensures the user enters a valid decimal number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("⚠️ Amount must be greater than zero.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a number (e.g., 1500.50).")

def get_valid_date(prompt):
    """Ensures the user enters a date in YYYY-MM-DD format."""
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid format. Use YYYY-MM-DD (e.g., 2024-01-15).")