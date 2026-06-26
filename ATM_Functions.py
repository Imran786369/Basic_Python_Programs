def My_ATM():
    balance=1000
    while True:
        print("**********ATM Menu**********")
        print("1.Deposit")
        print("2.Withdrawl")
        print("3.Balance Enquiry")
        print("4.Exit")
        choice = int(input("Pls enter your choice: "))
        if choice == 1:
            amount=float(input("Pls enter the deposit amount :"))
            if amount>0:
                balance+=amount
                print(amount, " Deposited to your account")
            else:
                print("Pls enter positive amount")
        elif choice == 2:
            amount = float(input("Pls enter the withdrawl amount : "))
            if amount<=balance:
                balance-=amount
                print(amount, " withdrain from your account")
            else:
                print("Insufficient funds in your account")
        elif choice == 3:
            print("Your current balance is : " , balance)
        elif choice == 4:
            print("Thank you! Pls visit again ")
            break
        else:
            print("Invalid choce entered")
My_ATM()