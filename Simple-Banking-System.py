balance = 10000
history = []
correct_pin = "1234"
attempts = 3
while True: 
    user_sec = input("Enter your PIN: ")
    if user_sec == correct_pin:
        print("banking menu open")
        break
    else:
        attempts -= 1
        print(f"worng pin {attempts} attempts left")
        if attempts == 0:
            print("Sorry pin not work")
            exit()
        
        
while True:

    print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Show History\n6. Exit ")
    try:
        user = int(input("chose: "))
        if user == 1:
            print(balance)
            
        elif user == 2:
            amount = int(input("Enter your Deposit Amount: "))
            if amount <= 0:
                print("Negative amount block")
                continue
            history.append(f"Deposited {amount} Tk")
            balance += amount
            print("Deposit Successfull.. " )
            print(f"Current Balance: {balance} Tk")
            
        elif user == 3:
            amount = int(input("Enter your Withdraw Amount: "))
            if amount <= 0:
                print("Negative amount block")
                print("Withdraw Failed")
            elif amount > balance:
                print("You don't have that much money in your account.")
            else:
                history.append(f"Withdrawn {amount} Tk")
                balance -= amount
                print("Withdraw Successfull.. " ) 
                print(f"Current Balance: {balance} Tk")   
                         
        elif user == 4:
            amount = int(input("Enter your Transfer Amount: "))
            if amount <= 0:
                print("Negative amount block Transfer Failed")

            elif amount > balance:
                print("You don't have that much money in your account.")
                
            else:    
                history.append(f"Transferred {amount} Tk")
                balance -= amount
                print("Transfer Successfull...")
                print(f"Current Balance: {balance} Tk")
        
        elif user == 5:
            if len(history) == 0:
                print("No transaction history found")
            else:
                for h in history:
                    print(h)

        elif user == 6:
            print("Thanks for using our Banking system ")
            break
           
        else:
            print("Please select 1, 2, 3,4,5 or 6 only")
            continue
    except:
        print("Enter valid number please (1.2.3.4) ")
        continue