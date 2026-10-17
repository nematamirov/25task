student_id = input("ID: ")
student_age = input("age: ")
disc_amount = 0
discounted = 0
if student_id.isascii() == False:
    print("only ascii")
elif len(student_id) != 8:
    print("only 8 charachters")
elif student_id.isdecimal() == False:
    print("only ascii digits")
else:
    if student_age.isascii() == False:
        print("ascii only")
    elif student_id.isdecimal() == False:
        print("ascii digits only")
    elif int(student_age) > 65 or int(student_age) < 16:
        print("not allowed")
    else:
        student_age = int(student_age)
        print("PY , WEB , CY")
        workshop_code = input("workshope code: ")
        match workshop_code:
            case "PY":
                
                if student_age < 16:
                    print("rejected")
                else:
                    if student_age <= 18 and student_age >= 16:
                        disc_amount = 20
                    pay_amount = input("pay amount: ")
                    if pay_amount.isascii() == False:
                        print("only ascii")
                    elif pay_amount.isdecimal() == False:
                        print("only ascii digits")
                    else:
                        pay_amount = int(pay_amount)
                        final_fee = 30 * (100 - disc_amount) / 100
                        if pay_amount < final_fee:
                            print("insufficient payment", final_fee - pay_amount , "is missing")
                        else:
                            discount = 30 * disc_amount / 100
                            print("registriaton confirmed", student_id , workshop_code , discount , final_fee , pay_amount - final_fee)

            case "WEB":
                disc_amount == 20 if (student_age <= 18 and student_age >= 16) else disc_amount == 0
                if student_age < 16:
                    print("rejected")
                else:
                    pay_amount = input("pay amount: ")
                    if pay_amount.isascii() == False:
                        print("only ascii")
                    elif pay_amount.isdecimal() == False:
                        print("only ascii digits")
                    else:
                        pay_amount = int(pay_amount)
                        final_fee = 40 * (100 - disc_amount) / 100
                        if pay_amount < final_fee:
                            print("insufficient payment", final_fee - pay_amount , "is missing")
                        else:
                            discount = 40 * disc_amount / 100
                            print("registriaton confirmed", student_id , workshop_code , discount , final_fee , pay_amount - final_fee)  
            case "CY":
                disc_amount == 20 if (student_age <= 18 and student_age >= 16) else disc_amount == 0
                if student_age < 18:
                    print("rejected")
                else:
                    pay_amount = input("pay amount: ")
                    if pay_amount.isascii() == False:
                        print("only ascii")
                    elif pay_amount.isdecimal() == False:
                        print("only ascii digits")
                    else:
                        pay_amount = int(pay_amount)
                        final_fee = 50 * (100 - disc_amount) / 100
                        if pay_amount < final_fee:
                            print("insufficient payment", final_fee - pay_amount , "is missing")
                        else:
                            discount = 50 * disc_amount / 100
                            print("registriaton confirmed", student_id , workshop_code , discount , final_fee , pay_amount - final_fee)
                

        