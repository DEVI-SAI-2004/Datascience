def generate_basic_report(expenses):
    """Calculates total and average spending from a list of expense dictionaries."""
    if not expenses:
        print("⚠️ No data available to generate report.")
        return

    total = sum(float(e['amount']) for e in expenses)
    count = len(expenses)
    average = total / count

    print("\n" + "="*30)
    print("📊 GENERAL SUMMARY")
    print("-" * 30)
    print(f"Total Expenses:  ₹{total:,.2f}")
    print(f"Number of Items: {count}")
    print(f"Average Spend:   ₹{average:,.2f}")
    print("="*30)

def generate_category_report(expenses):
    """Groups expenses by category and displays the breakdown."""
    if not expenses:
        return

    category_totals = {}
    for e in expenses:
        cat = e['category']
        amt = float(e['amount'])
        category_totals[cat] = category_totals.get(cat, 0) + amt

    print("\n🍱 CATEGORY-WISE BREAKDOWN")
    print("-" * 30)
    for cat, total in category_totals.items():
        print(f"{cat:<15}: ₹{total:,.2f}")
    print("-" * 30)