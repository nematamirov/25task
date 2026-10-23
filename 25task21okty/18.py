acc_pin = 2580
balance = 1000
fail_attempt = 0
while fail_attempt < 3:
    passw = int(input())
    if passw != acc_pin:
        print("Wrong pass try again")
        fail_attempt = fail_attempt + 1
    else:
        print("welcoe")
        print("""
        1 - show balance
        2 - add amount
        3 - subtract amount
        4 - bye
        """)
        option = int(input("Choose one: "))
        while option != 4:
            if option == 1:
                print("Balance")
            elif option == 2:
                add_amount = float(input("Write amount: "))
                if add_amount == 0 or add_amount < 0:
                    print("wrong")
                else:
                    balance = balance + add_amount
            elif option == 3:
                sub_amount = float(input())
                if sub_amount < 0 or sub_amount > balance:
                    print("wrong")
                else:
                    balance = balance - sub_amount
            else:
                print("INvalid")
        print("bye")        
            