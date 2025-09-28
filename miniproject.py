print("WELCOME TO SBI ATM")
balance = 10000
pin=int(input("enter your pin"))
if (pin == 123):
    choice= int(input("enter 1 for withdraw, 2 for deposit, 3 for balance, 4 for exit:"))
    if (choice == 1):
        amount= int(input("enter the amount to withdraw"))
        balance= balance + amount
        print("your balance is", balance)
    elif (choice == 2):
        amount= int(input("enter the amount to deposit"))
    elif (choice == 3):
        amount= int(input("check amount"))