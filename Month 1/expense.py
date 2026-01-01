class Expense:
    def __init__(self, amount, category, date, description):
        """
        Initializes an Expense object.
        Technical Requirement: attributes for amount, category, date, description.
        """
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description
    
    def to_dict(self):
        """Converts object attributes to a dictionary for CSV writing."""
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }

    def __str__(self):
        """Returns a user-friendly string representation of the expense."""
        return f"[{self.date}] {self.category}: ₹{self.amount:.2f} ({self.description})"