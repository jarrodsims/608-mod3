# custom-object-jarrodsims.py
"""program to calculate tax and tip."""

class Purchase(object):
    def __init__(self, amount):
        self.amount = amount

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

# Create purchase object given an amout
purchase = Purchase(100.0)

# set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

# Use the object to calculate tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

# Display tax, tip, and total
print('Tax:', tax)
print('Tip:', tip)
print('Total:', purchase.calculateTotal(taxPercent, tipPercent))