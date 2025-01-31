from datetime import datetime
Balance = 10000 #10900 #5900
user_pin = None # 1234 -> 1432
inserted = False # True # False
blocked = False 
attempt = 0 #1 #2 #3
transactions = [] # [1000, -100, -5000 ]
print("Welcome to SBI") #john@pentagonspace.in

while True:
    if inserted == False:
        print("Insert the card")
        x = int(input("1 - Inserted or 2 - for not Inserted"))
        if x == 1:
           inserted = True
    if not user_pin:
        user_pin = int(input("Set the PIN : "))
    if blocked == True:
        print("Your Card has been blocked, contact your Branch manager to unblock")
        break
    enter_pin = int(input("Enter your PIN : ")) 

    if enter_pin == user_pin:
        print(
    """
        1. Deposit
        2. Withdrawal
        3. Mini Statement
        4. PIN Change
    """
        )
        option = int(input("Select any one of the options above :"))
        if option == 1:
            amount = int(input("Enter the amount : "))
            if amount % 100 == 0:
                print("Cash has been accepted")
                Balance = Balance + amount
                transactions.append(amount)
                print("Available Balance is ", Balance)
            else:
                print("Invalid Cash or feed only multiples of 100")
        if option == 2:
            amount = int(input("Enter the amount : "))
            if amount < Balance:
                if amount % 100 == 0:
                    print("Take the Cash")
                    Balance = Balance - amount
                    transactions.append(-amount)
                    print("Available Balance is ", Balance)
                else:
                    print("Invalid Cash or feed only multiples of 100")
            else:
                print("Insufficient Balance")

        if option == 3:

            datim = datetime.now()

            date = datim.strftime("%d-%m-%Y")

            time = datim.strftime("%I:%M %p")
            print(

                f"""
                                State Bank of India
                Date: {date}                                       Time: {time}

                Last Transactions: """)
            
            for t in transactions:
                print(f"""                                       {t}""")
                                        

            print(f"""Available Balance:      {Balance}

                """
            )
        if option == 4:
            old_pin = int(input("Enter Old PIN : "))
            if old_pin == user_pin:
                user_pin = int(input("Enter New PIN : "))
            else:
                print("Invalid PIN, Try again")
                continue


    else:
        attempt += 1
        print("Invalid PIN, Try again")
        if attempt >=2:
            blocked = True


    cont = input("Do you want to continue 1 for yes and enter for no")

    if cont == '1':
        continue
    elif cont=='':
        print("Thank you for visiting SBI ....")
        inserted = False 






