"""
Open the ATM.py file using any IDE or copy/paste
the code. Run it. Make sure the card.json is in the
same directory as ATM.py
The json also updates after transaction. Open the two
files side-by-side to observe the effect
"""

import time, os, json

cash_in_machine = 10000
clear = lambda: os.system("cls")

def mainMenu():
    print("\nCurrent account <c>")
    print("Savings account <s>")
    acc = input("Make transaction using: ")
    if acc == 's': print("\nHaraam")
    elif acc == 'c':
        amount = askAmount()
        withdrawal = withdraw(amount)
        if withdrawal == 1:
            with open("card.json", "w") as file:
                json.dump(card, file,  indent=4)
    else: mainMenu()

def askAmount():
    print("\n1. 1000\t\t2. 2000")
    print("3. 3000\t\t4. 4000")
    print("5. 5000\t\t6. Other amount")
    option = input("Select from the above options: ")
    if option == "1": return 1000
    elif option == "2": return 2000
    elif option == "3": return 3000
    elif option == "4": return 4000
    elif option == "5": return 5000
    elif option == "6":
        amount = int(input("\nEnter the amount you want to withdraw: "))
        return amount
    else: return askAmount()

def withdraw(amount: int):
    global cash_in_machine
    if amount > card["balance"]:
        print("\nInsufficiant balance")
    elif amount > cash_in_machine:
        print("\nInsufficiant cash in machine")
    elif amount % 500 != 0:
        print("\nAmount must be a multiple of 500")
    else:
        card['balance'] -= amount
        cash_in_machine -= amount
        print("\nWithdrawal successful")
        return 1
    return 0

with open("card.json") as file:
    card = json.load(file)

clear()
print("Card in...\n")
time.sleep(0.5)

pin = input("Enter a 4-digit pin: ")
if pin == str(card["pin"]): mainMenu()
else: print("\ninvalid pin")

time.sleep(0.5)
print("\nCard out...")
time.sleep(0.5)