# helpers.py

def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity * price

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

# Functions operate on data
def clean_text(text):
    return text.strip().lower()

def remove_punctuation(text):
    return text.replace(".", "").replace(",", "")

