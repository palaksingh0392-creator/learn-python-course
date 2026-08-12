#Challenge 1: ATM Program
# Start with a balance such as Rs 10,000.
# Menu: Check Balance, Deposit, Withdraw, Exit.
# Do not allow withdrawal above the balance or an amount less than or equal to 0.
# Keep showing the menu until Exit is selected

name = input("enter your name, please :")
account = int(input("enter your account number :"))
balance = 10000
while True :
    print(
    "Enter the valid choice: "
    "1 - Check Balance, "
    "2 - Deposit, "
    "3 - Withdrawal, "
    "4 - Exit: "
    )

    choice = int(input("enter valid choice: "))


    match choice :
    #choice selection
    #case 1 : check balance
        case 1 :
                print(f"the balance in account no {account} is {balance} ")
    #case 1 : deposit
        case 2 :
            deposit = float(input("enter the deposit amount:"))
            if deposit > 0:
                balance = balance + deposit 
                print(f"your amount{deposit} has successfully deposited")
            else :
                print("enter valid amount")
                deposit = float(input("enter the deposit amount:"))
    #case 1 : withdrawl
        case 3:
            draw = float(input("enter the Withdrawal amount:"))
            if draw < balance or draw > 0:
                balance = balance - draw
                print(f"your amount{draw} has successfully withdrawl")
            else:
                print("enter valid amount")
                draw = float(input("enter the Withdrawal amount:"))  
    #case 1 : exit
        case 4:
            print("your transactions are upto date")
            break


