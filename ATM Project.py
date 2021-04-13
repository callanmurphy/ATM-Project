#ATM Project – Callan Murphy
#01/04/2019
#Bonus 1 and 2 Completed
'''
NOTE on Bonuses: The program will save a card number and PIN number,
storing a single user's account. It will save 3 balances for checking,
savings and investments (3 individual sub-accounts within the main one)
and one overall overdraft amount to be used by all 3 of the sub-accounts.
(For example, if a user creates an account, ending the program with a
balance of $0 in checking, $567.33 in savings, $250.87 in investments,
and $600.00 in overdraft, when they restart the program and sign into
their accout, those values will be the same).
'''

'''  
Our ATM program begins by asking to user if they wish to create an account.
If they have created an account previously, they can input 'no' and sign in
with their previous details (Bonus 1/2). Otherwise, an account must be created.  
'''
#coloured text is used throughout the program to make headings and important information more visible to the user

def checkMoney(inputMoney):
  '''
  Function to ensure that float variables are stored correctly as integer variables and string inputs are known to the user as invalid.
  '''
  if str.find(inputMoney, ".") != -1: #checks if a decimal exists in the input
      inputMoney = float(inputMoney) #converts string to float
      round(inputMoney, 2) #rounds float to 2 decimal places in case the user inputted more than 2
      inputMoney = inputMoney * 100 #multiplies the input by 100 to store it as in integer (later to be divided when outputted)
      inputMoney = int(inputMoney) #makes input an integer
      return inputMoney
  else:
      if inputMoney.isdigit(): #checks if the input was an integer
          inputMoney = int(inputMoney) #converts string to int
          inputMoney = inputMoney * 100 #multiplies it to store the amount correctly
          if inputMoney > -1: #fixes error with user inputting negative number
              return inputMoney
      else: #in case the user inputs a string or another incorrect input
          print(   "Not a valid input! Must be a positive integer value" + "  ")
          inputNum = "Error"
          return inputNum

def checkInt(inputNum):
  '''
  Function to ensure that input is specifically an integer.
  '''
  if inputNum.isdigit(): #checks if input is integer
      inputNum = int(inputNum) #converts string to int
      if inputNum > -1: #fixes error with user inputting negative number
          return inputNum
      else:
          print(   "Not a valid input! Must be a positive value" + "  ")
          inputNum = "Error"
          return inputNum
  else: #tells user that the input must be an integer
      print(   "Not a valid input! Must be an integer!" + "  ")
      inputNum = "Error"
      return inputNum

def newPin():
  '''
  Function to create a new PIN.
  '''
  while True:
      pinNumber = input("Enter a new 4-digit PIN number for your account:")
      pinNumber = checkInt(pinNumber) #calls function to ensure input is an integer
      if len(str(pinNumber)) != 4: #ensures that input is 4 digits
          print(   "PIN must be 4 digits!" + "  ")
      elif pinNumber != "Error":
          break
  return pinNumber

def newCard(noAccount):
  '''
  Function to create new card/account.
  '''
  while True:
      createNew = input("Do you wish to create a new account? (yes/no):") #user does not have to if an account already exists from a previous run of the program
      createNew = str.lower(createNew) #input made lowercase in case the user inputs a capital letter
      if createNew == "yes": #runs through process of creating new account
          totalWithdrawal = 0 #variable to be used later for total of withdrawals
          totalDeposit = 0 #variable to be used later for total of depositis
          while True:
              cardNumber = input("Enter your new card number (any number of digits):")
              cardNumber = checkInt(cardNumber) #calls function to ensure input is an integer
              if cardNumber != "Error":
                  break
          pinNumber = newPin() #calls newPin function for user to create a PIN
          while True:
              overdraftOption = input("Do you wish to sign up for overdraft protection? (yes/no):")
              overdraftOption = str.lower(overdraftOption)
              if overdraftOption == "yes":
                  break
              if overdraftOption == "no":
                  overdraft = 0 #since the user does not wish to have overdraft, its value is set to 0
                  break
              else: #ensures that user inputs the correct input
                  print(   "Not a valid input! Please enter 'yes' or 'no'!" + "  ")
          if overdraftOption == "yes": #overdraft options are displayed
              print()
              print("Our options for overdraft protection are as follows...")
              print("$250")
              print("$500")
              print("$1000")
              print("$2500")
              print("$5000")
              while True:
                  overdraft = input("Please enter the amount of overdraft you wish to recieve: $")
                  overdraft = checkInt(overdraft) #calls function to ensure input is an integer
                  if overdraft != 250 and overdraft != 500 and overdraft != 1000 and overdraft != 2500 and overdraft != 5000:
                      print(   "Not a valid input! Must be one of the amounts listed above!" + "  ")
                      #ensures that input is proper
                  else:
                      overdraft = overdraft * 100 #stores the overdraft variable correctly (by multiplying it by 100)
                      break
          f = open('BankRecords.txt', 'w') #creates a text file to store user data
          f.write(str(cardNumber))
          f.write("\n") #new line
          f.write(str(pinNumber))
          f.write("\n")
          f.write(str(overdraft))
          f.write("\n")
          f.write("0") #balance value for a sub-account (checking)
          f.write("\n")
          f.write("0") #balance value for a sub-account (savings)
          f.write("\n")
          f.write("0") #balance value for a sub-account (investments)
          f.write("\n")
          f.close()
          # code above done with help from youtube video
          # https://youtu.be/f6zeuk5UjuE
          break
      elif createNew == "no" and noAccount == 0: #noAccount variable ensures that an account already exists
          break
      else: #prints error statement for improper input
          print(   "Not a valid input! Please enter 'yes' or 'no' ('no' can only be inputted if there is an existing account)" + "  ")
  lines = [] #creates a list for the lines in the text file
  f = open('BankRecords.txt', 'r')
  for line in f:
      values = line.split() #splits the lines of the textfile
      lines.append(values) #this loop creates a list seperating each line of the textfile
  # code above done with help from StackOverflow
  # https://stackoverflow.com/questions/28700849/difference-between-readlines-and-split-python
  cardNumber = int(''.join(filter(str.isdigit, lines[0]))) #each of these lines assigns the textfile information to a variable in the program
  pinNumber = int(''.join(filter(str.isdigit, lines[1]))) #the long strand of confusing code is to take only the digits from the line from the textfile
  overdraft = int(''.join(filter(str.isdigit, lines[2])))
  checking = int(''.join(filter(str.isdigit, lines[3])))
  savings = int(''.join(filter(str.isdigit, lines[4])))
  investments = int(''.join(filter(str.isdigit, lines[5])))
  # code for the above line was formed with help from StackOverflow
  # https://stackoverflow.com/questions/26825729/extract-number-from-string-in-python/26825781
  totalDeposit = 0
  totalWithdrawal = 0
  loginSystem(cardNumber, pinNumber, overdraft, totalWithdrawal, totalDeposit, checking, savings, investments)


def viewDetails(balance, cardNumber, overdraft):
  '''
  Function to view the account details.
  '''
  print(   "Details" + "  ")
  print("Card Number:", cardNumber)
  print()
  print("Balance: $" + str(balance/100)) #data is converted to a string for better formatting and divided since it is stored as * 100
  print("Overdraft Protection: $" + str(overdraft/100))

def withdrawal(balance, overdraft, totalWithdrawal):
  '''
  Function for the user to withdrawal money.
  '''
  print(   "Withdrawal" + "  ")
  print("The options for a withdrawal are as follows...")
  print("[1]: $20")
  print("[2]: $40")
  print("[3]: $60")
  print("[4]: $80")
  print("[5]: $100")
  print("[6]: $120")
  print("[7]: Other")
  while True:
      breakLoop = 0  # variable required to later break out of nested loop correctly
      withdrawalFundCheck = 0  # variable to later check if funds are sufficient
      while True:
          withdrawalOptions = [2000, 4000, 6000, 8000, 10000, 12000, 0]  # stored as * 100 their values one again
          totalBalance = balance + overdraft  # creates one balance of both the sub-account balance and the overdraft
          while True:
              withdrawalSelect = input("Enter an option from 1-7:")
              withdrawalSelect = checkInt(withdrawalSelect)  # calls functions to check that input is int
              if withdrawalSelect != "Error":
                  break
          if withdrawalSelect <= 0 or withdrawalSelect >= 8:  # makes sure that input is valid (1-7)
              print(   "Must input an option from the list above!" + "  ")
          elif withdrawalSelect != "Error":
              break
      for i in range(0, 7):  # loop of 7 for each possible input option
          if withdrawalSelect == i + 1 and totalBalance >= withdrawalOptions[i]:  # checks that account has enough money for withdrawal
              withdrawalFundCheck = 1  # variable to later check if funds are sufficient
              if withdrawalSelect == 7:  # since '7 = other', it needs specific commands
                  print()
                  while True:
                      withdrawalSelect = input("Enter the desired withdrawal amount: $")
                      withdrawalSelect = checkMoney(withdrawalSelect)
                      if withdrawalSelect != "Error":
                          if totalBalance < withdrawalSelect:  # checks that there is enough money for withdrawal
                              withdrawalSelect = str(withdrawalSelect)
                              withdrawalSelect = "Error"
                              print(   "Insufficient funds!" + "  ")
                          else:
                              withdrawalOptions[i] = withdrawalSelect

                              break
                      else:
                          print(   "Not a valid input!" + "  ")
              balance = balance - withdrawalOptions[i]  # removes withdrawal amount from balance
              totalWithdrawal += withdrawalOptions[i]  # increases withdrawal total (for history of withdrawals)
              print()
              print("  " + "Dispensing $" + str(withdrawalOptions[i] / 100) + "  ")
              if balance < 0:  # if balance is in the negatives it will be reverted to 0
                  overdraft = overdraft + balance  # the amount by which balance is in the negatives by will be taken from the overdraft instead (to maintain positive values and proper amount)
                  balance = 0
              print("Balance: $" + str(balance / 100))  # divided by 100 due to proper storage of variables
              print("Overdraft $" + str(overdraft / 100))
      if withdrawalFundCheck == 0:  # checks to make sure the account has enough money for withdrawal
          print(   "Insufficient funds!" + "  ")
      print()
      while True:
          continueWithdrawal = input(
              "Do you wish to withdrawal more money? (yes/no)")  # allows the user to make multiple withdrawals
          if continueWithdrawal == "no":
              break
          elif continueWithdrawal == "yes":
              breakLoop = 1  # required to break nested loop
              break
          else:
              print(   "Not a valid input! Please enter 'yes' or 'no'" + "  ")
      if breakLoop == 0:
          return balance, overdraft, totalWithdrawal

def history(balance, cardNumber, overdraft, totalWithdrawal, totalDeposit, allBills):
  '''
  Function to print history of transactions.
'''
  print(   "History" + "  ")
  print("Account Created:", cardNumber)
  print()
  print("Total Deposit Amount: $" + str(totalDeposit / 100))
  print("Total Withdrawal Amount: $" + str(totalWithdrawal / 100))
  print("Bills Paid:", allBills)
  return (balance, overdraft)


def startUp():
  '''
  Function to begin the program.
  '''
  noAccount = 0 #variable for knowing if an account exists
  import os #required import to check if file exists
  if os.path.isfile('BankRecords.txt') == False: #checks if the file exists so that the program knows later on
      # above code was done with help from StackOverflow
      # https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists
      noAccount = 1
  print(   "*" * 35 + "  ")
  print(   "Welcome to the incredible ATM 9000!" + "  ")
  print()
  print(   "Begin by creating an account below..." + "  ")
  print(   "*" * 35 + "  ")
  newCard(noAccount)


# Jonathan


def loginSystem(cardNumber, pinNumber, overdraft, totalWithdrawal, totalDeposit, checking, savings, investments):
    allBills = []
    '''
    Creates empty bill list for later usage.
    '''
    print()
    print("-" * 30)
    print("Login")
    print("-" * 30)
    while True:
        cardNumberInput = input("Enter your card number:")
        cardNumberInput = checkInt(cardNumberInput)
        if cardNumberInput == cardNumber: #comparing inputted number to actual card number
            #code for the above line was formed with help from StackOverflow
            break
        else:
            print(   "Your card number is incorrect. Please try again" + "  ")
    pinAttempts = 0
    while True:
        pinInput = input("Enter your pin:")
        pinInput = checkInt(pinInput)
        if pinInput == pinNumber: #comparing inputted number to PIN
            #code for the above line was formed with help from StackOverflow
            print()
            print("Access Granted")
            print()
            accountChoice(cardNumber, pinNumber, overdraft, totalDeposit, totalWithdrawal, checking, savings, investments, allBills)
            break
        else:
            print("Your PIN was incorrect, please try again")
            pinAttempts = pinAttempts + 1
        if pinAttempts == 3:
            print("You have failed your PIN three times. Your account has been locked, please try again another day" + "  ")
            break




def accountChoice(cardNumber, pinNumber, overdraft, totalWithdrawal, totalDeposit, checking, savings, investments, allBills):
  '''
  Allows the user to choose their account.
  '''
  while True:
      userChoice = input("Would you like to access your checking, savings, or investments account?")
      str.lower(userChoice)
      if userChoice == "checking":
          account = "checking"
          balance = checking
          menu(balance, cardNumber, pinNumber, overdraft, totalDeposit, totalWithdrawal, checking, savings, investments, account, allBills)
          break
      elif userChoice == "savings":
          account = "savings"
          balance = savings
          menu(balance, cardNumber, pinNumber, overdraft, totalDeposit, totalWithdrawal, checking, savings, investments, account, allBills)
          break
      elif userChoice == "investments":
          account = "investments"
          balance = investments
          menu(balance, cardNumber, pinNumber, overdraft, totalDeposit, totalWithdrawal, checking, savings, investments, account, allBills)
          break
      else:
          print(   "Please input either 'checking', 'savings' or 'investments'" + "  ")

def menu(balance, cardNumber, pinNumber, overdraft, totalWithdrawal, totalDeposit, checking, savings, investments, account, allBills):
  '''
  The main menu function for the program.
  '''
  while True:
      print()
      print("-" * 25)
      print(   "MAIN MENU" + "  ")
      print("")
      print("[1]: View your account details")
      print("[2]: Change your PIN")
      print("[3]: Withdraw funds")
      print("[4]: Deposit funds")
      print("[5]: Print your history")
      print("[6]: Pay bills")
      print("[7]: Change your account")
      print("[8]: Exit Machine")
      print("-" * 25)
      userChoice = input("Enter an option from 1-8:")
      if userChoice == "1":
          print()
          viewDetails(balance, cardNumber, overdraft)
      elif userChoice == "2":
          print()
          changePin(pinNumber)
      elif userChoice == "3":
          print()
          balance, overdraft, totalWithdrawal = withdrawal(balance, overdraft, totalWithdrawal)
      elif userChoice == "4":
          print()
          balance, totalDeposit = deposit(balance,totalDeposit)
      elif userChoice == "5":
          print()
          history(balance, cardNumber, overdraft, totalWithdrawal, totalDeposit, allBills)
      elif userChoice == "6":
          print()
          balance,overdraft, allBills = payBills(balance, overdraft, allBills)
      elif userChoice == "7":
          print()
          accountChoice(cardNumber, pinNumber, overdraft, totalWithdrawal, totalDeposit, checking, savings, investments, allBills)
          break
      elif userChoice == "8":
          if account == "checking":
              checking = balance
          elif account == "savings":
              savings = balance
          elif account == "investments":
              investments = balance
          f = open('BankRecords.txt', 'w')
          f.write(str(cardNumber))
          f.write("\n")
          f.write(str(pinNumber))
          f.write("\n")
          f.write(str(overdraft))
          f.write("\n")
          f.write(str(checking))
          f.write("\n")
          f.write(str(savings))
          f.write("\n")
          f.write(str(investments))
          f.write("\n")
          f.close()
          print("")
          print(   "Thank you for using the ATM 9000 today!" + "  ")
          print(   "ATM exited" + "  ")
          break
      else:
          print(   "Please enter an option from 1-8" + "  ")

def changePin (pinNumber):
  '''
  Function to change the pin.
  '''
  while True:
    oldPin = input("Please enter the old PIN you wish to change:")
    oldPin = checkInt(oldPin)
    if oldPin != pinNumber:
      print(   "Your old PIN was incorrect. Please try again" + "  ")
    elif oldPin == pinNumber:
      newPinNumber = newPin ()
      print()
      print("  " + "PIN successfully changed!" + "  ")
      break
  return newPinNumber


def deposit (balance,totalDeposit):
  '''
  Function to deposit funds.
  '''
  while True:
    amountDeposited = input("How much would you like to deposit? $")
    amountDeposited = checkMoney(amountDeposited)
    if amountDeposited == "Error":
      amountDeposited = 0
    balance = balance + amountDeposited
    totalDeposit = totalDeposit + amountDeposited
    while True:
      userChoice = input("Would you like deposit another amount? [Yes/No]").lower()
      if userChoice != "yes" and userChoice != "no":
        print(   "Please input either yes or no." + "  " )
      elif userChoice == "no":
        break
      elif userChoice == "yes":
        break
    if userChoice == "no":
      break
  return balance, totalDeposit

def payBills(balance, overdraft, allBills):
  billName = input("What bill would you like to pay?")
  totalBalance = balance + overdraft
  while True:
    billAccountNumber = input("Enter your account number for this bill")
    billAccountNumber = checkInt(billAccountNumber)
    if billAccountNumber != "Error":
      break
  while True:
    amountPaid = input("How much would you like to pay towards this bill? $")
    amountPaid = checkMoney(amountPaid)
    if amountPaid != "Error":
        if totalBalance >= amountPaid:
          balance = balance - amountPaid
          print("  " + "Bill successfully paid" + "  ")
          if balance < 0:
              overdraft = overdraft + balance
              balance = 0
          break
        else:
          print(   "You have insufficient funds to make this payment" + "  ")
  totalBills = str(billName) +    str(billAccountNumber) + " $" + str(amountPaid/100)
  allBills.append(totalBills)
  return balance, overdraft, allBills















startUp()






