class Category:
    def __init__(self, name):
      self.name = name
      self.ledger = list()
      self.balance = 0

    def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})
      self.balance = self.balance + amount
#      self.statement_line()

    def check_funds(self, amount):
      if self.balance >= amount:
        return True
      else:
        return False

    def withdraw(self, amount, description=""):
      if self.check_funds(amount) == False:
        return False
      self.ledger.append({"amount": -amount, "description": description})
      self.balance = self.balance - amount
#      self.statement_line()
      return True

    def get_balance(self):
      return self.balance

    def statement_line(self):
      print("Balance in " + self.name + " is now " + str(self.get_balance()))

    def transfer(self, amount, recipient):
      if not isinstance(recipient, Category):
        print("Error: no such category to transfer to.")
        return False
      if self.check_funds(amount) == False:
#        print("Transfer cancelled due to insufficient funds.")
        return False
      desc_to = "Transfer to " + recipient.name
      desc_from = "Transfer from " + self.name
      self.withdraw(amount, desc_to)
      recipient.deposit(amount, desc_from)
#      self.statement_line()
#      recipient.statement_line()
      return True

    def __str__(self):
      allstars = 30-len(self.name)
      leftstars = allstars // 2
      ritestars = leftstars + allstars % 2
      printout = "*"*leftstars + self.name + "*"*ritestars
      for dict in self.ledger:
        amount = dict["amount"]
        description = dict["description"]
        description = description[:23]
        amtstr = f'{amount:.2f}'
        thisrow = f'{description : <23}' + f'{amtstr:>7}'
        printout = printout + "\n" + thisrow
      printout = printout + "\n" + "Total: " + f'{self.balance:.2f}'
      return printout

def create_spend_chart(categories):
  numcols = len(categories)
  allspent={}
  totspent=0
  if numcols > 4:
    return "Error: too many categories"
  numrows = max(len(cat.name) for cat in categories) + 13
  starry = ["" for i in range(numrows)]
  for i in range(11):
    pcnt = (10-i)*10
    starry[i] = f'{str(pcnt)+"|" : >4}'
  starry[11] = " "*4 + "-"*(3*numcols+1)
  for i in range(12, numrows):
    starry[i] = " "*4
  outstring = "Percentage spent by category"
  for cat in categories:
    total_out = 0
    for dict in cat.ledger:
      amount = dict["amount"]
      if amount < 0:
        total_out = total_out - amount
    allspent[cat.name] = total_out
  totspent = sum(allspent.values())
  # print(allspent)
  for cat in categories:
    catnam = cat.name
    catlen = len(catnam)-1
    pcspent = allspent[catnam] / totspent
    # pcround = round(100*pcspent,-1)
    pcround = int(10*pcspent)*10
  #  print(pcround)
    for i in range(11):
      pcnt = (10-i)*10
      if pcround >= pcnt:
        starry[i] = starry[i] + " o "
      else:
        starry[i] = starry[i] + " "*3
    for i in range(12, numrows-1):
      l = i-12
      if l <= catlen:
        starry[i] = starry[i] + " " + catnam[l] + " "
#        starry[i] = starry[i] + " " + str(l) + " "
      else:
        starry[i] = starry[i] + " "*3
  outstring = outstring + "\n" + " \n".join(starry)
  outstring = outstring.replace("--- ","---")+" "
  return outstring.rstrip()+"  "