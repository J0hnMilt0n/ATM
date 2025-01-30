Balance = 10000
user_pin = None # 1234
inserted = False # True # False
blocked = False 
attempt = 0 #1 #2 #3
print("Welcome to SBI")
user_pin = int(input("Set the PIN : "))

while True:
    if inserted == False:
        print("Insert the card")
        x = int(input("1 - Inserted or 2 - for not Inserted"))
        if x == 1:
           inserted = True
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
                print("Available Balance is ", Balance)
            else:
                print("Invalid Cash or feed only multiples of 100")
        if option == 2:
            amount = int(input("Enter the amount : "))
            if amount < Balance:
                if amount % 100 == 0:
                    print("Take the Cash")
                    Balance = Balance - amount
                    print("Available Balance is ", Balance)
                else:
                    print("Invalid Cash or feed only multiples of 100")
            else:
                print("Insufficient Balance")

    else:
        attempt += 1
        print("Invalid PIN, Try again")
        if attempt >=2:
            blocked = True


    cont = input("Do you want to continue 1 for yes and enter for no")

    if cont == '1':
        continue
    elif cont=='':
        inserted = False 

print("Thank you for visiting SBI ....")




