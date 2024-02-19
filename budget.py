class Category:

  # Constructing category with empty ledger
  def __init__(self, category):
    self.category = category
    self.ledger = []

  # Title line of 30 characters, centred
  # In a line of * characters
  # A lsit of items in the ledger (new line)
  # Each line shows description and amount
  # First 23 characters of the description, then amount
  # Amount is right aligned & two decimal places, max 7 characters
  # Line with catagory total

  def __str__(self):
    text = self.category.center(30, '*') + "\n"
    for item in self.ledger:
      a = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      text += a + "\n"
    text += 'Total: ' + str(self.get_balance())
    return text

  # Deposit method accepts amount and description
  # No amount = empty string

  def deposit(self, amount, description=''):
    temp = {}
    temp['amount'] = amount
    temp['description'] = description
    self.ledger.append(temp)

  # Withdraw method
  # Stored in ledger as -ve
  # Returns TRUE if withdrawal took place, otherwise FALSE

  def withdraw(self, amount, description=''):
    temp = {}
    if self.check_funds(amount):
      temp['amount'] = -amount
      temp['description'] = description
      self.ledger.append(temp)
      return True
    return False

  # Get balance method

  def get_balance(self):
    return sum(item['amount'] for item in self.ledger)

  # Transfer method

  def transfer(self, amount, expense_cat):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + expense_cat.category)
      expense_cat.deposit(amount, "Transfer from " + self.category)
      return True
    return False

  # Check funds method
  # Amount > balance == False
  # Method needs to be used by both withdraw and transfer method

  def check_funds(self, amount):
    return amount <= self.get_balance()

  # Create spend list
  # Total amount spent == -ve
  # Iterates over categories list
  # Sum up values in spend
  # Percentage of total spending for each category and stores it as an integer


def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  total = sum(spend)
  percentage = [i / total * 100 for i in spend]

  # Loop from 100 to 0 in steps of -10
  # Appends line to chart with percentage label i
  # O if percentage > i

  j = "Percentage spent by category"
  for i in range(100, -1, -10):
    j += "\n" + str(i).rjust(3) + "|"
    for a in percentage:
      if a > i:
        j += " o "
      else:
        j += "   "
    j += " "
  j += "\n" + "    "

  for i in percentage:
    j += "-" * 3
  j += "-"

  # Empty category string
  # Max length
  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  # Spacing
  for m in range(max_length):
    j += "\n    "
    for c in range(len(categories)):
      if m < cat_length[c]:
        j += " " + categories[c].category[m] + " "
      else:
        j += "   "
    j += " "

  return j
