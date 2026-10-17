a = int(input())
b = int(input())
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print("Equal")
# #--------------------------
a = float(input())
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")
# #--------------------------
a = int(input())
if a % 2 == 0:
    print("Even")
else:
    print("Odd")
# #--------------------------
a = int(input())
if a >= 0 and a <= 50:
    print("F")
elif a > 50 and a <= 60:
    print("E")
elif a > 60 and a <= 70:
    print("D")
elif a > 70 and a <= 80:
    print("C")
elif a > 80 and a <= 90:
    print("B")
elif a > 90 and a <= 100:
    print("A")
else:
    print("Invalid score")
# #--------------------------
a = float(input())
b = float(input())
c = float(input())
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
# #--------------------------
a = float(input())
b = float(input())
print("+,-,*,/,%,**,//")
op_input = input()
match op_input:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b == 0:
            print("Invalid")
        else:
            print(a / b)
    case "%":
        if b == 0:
            print("Invalid")
        else:
            print(a % b)
    case "**":
        if a == 0 and b < 0:
            print("Invalid")
        elif a < 0 and b % 1 != 0:
            print("Invalid")
        else:
            print(a ** b)
    case "//":
        if b == 0:
            print("Invalid")
        else:
            print(a // b)
# #--------------------------
a = int(input())
if a >= 0 and a <= 12:
    print("Child")
elif a >= 13 and a <= 17:
    print("Teenager")
elif a >= 18 and a <= 64:
    print("Adult")
elif a > 64:
    print("Senior")
else:
    print("Invalid age")
# #--------------------------
org_price = float(input())
if org_price < 100:
    disc_amount = 0
    print(org_price)
    print(disc_amount)
    print(org_price*(100-disc_amount)/100)
elif org_price >= 100 and org_price < 300:
    disc_amount = 10
    print(org_price)
    print(disc_amount)
    print(org_price*(100-disc_amount)/100)
elif org_price >= 300 and a < 500:
    disc_amount = 15
    print(org_price)
    print(disc_amount)
    print(org_price*(100-disc_amount)/100)
elif org_price >= 500:
    disc_amount = 20
    print(org_price)
    print(disc_amount)
    print(org_price*(100-disc_amount)/100)
else:
    print("Invalid input")
# #----------------------------------
a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
    smallest = a
    if a > b and a > c:
        biggest = a
    elif b > a and b > c:
        biggest = b
        mid = c
    else:
        biggest = c
        mid = b
elif b < a and b < c:
    smallest = b
    if a > b and a > c:
        biggest = a
        mid = c
    elif b > a and b > c:
        biggest = b
    else:
        biggest = c
        mid = a
else:
    smallest = c
    if a > b and a > c:
        biggest = a
        mid = b
    elif b > a and b > c:
        biggest = b
        mid = a
    else:
        biggest = c
print(smallest, mid , biggest)
#----------------------------------
acc_balance = 1000
withdraw = float(input())
rem_balance = acc_balance - withdraw
if withdraw <= 0:
    print("Invalid amount")
elif rem_balance < 0:
    print("Insufficient balance")
else:
    print(rem_balance)
# #-------------------------------------
monthly_usage = float(input())
if monthly_usage >= 0 and monthly_usage <= 100:
    applied_rate = 0.08
    print(monthly_usage)
    print(applied_rate)
    print(monthly_usage*applied_rate)
elif monthly_usage > 100 and monthly_usage <= 300:
    applied_rate = 0.12
    print(monthly_usage)
    print(applied_rate)
    print(monthly_usage*applied_rate)
elif monthly_usage > 300 
    applied_rate = 0.15
    print(monthly_usage)
    print(applied_rate)
    print(monthly_usage*applied_rate)
else:
    print("Invalid")
# #----------------------------------------
distance = float(input())
start_fee = 2
if distance >= 0 and <= 5:
    dist_fee = 0.70
    print(start_fee)
    print(dist_fee)
    print(start_fee + dist_fee*distance)
elif distance > 5 and <= 15:
    dist_fee = 0.60
    print(start_fee)
    print(dist_fee)
    print(start_fee + dist_fee*distance)
elif distance > 15:
    dist_fee = 0.50
    print(start_fee)
    print(dist_fee)
    print(start_fee + dist_fee*distance)
else:
    print("Invalid")
# #---------------------------------------
user_age = int(input())
salary = float(input())
req_loan = float(input())
xyz = salary*10 
if user_age < 18 or salary < 500 or req_loan > xyz:
    print("REJECTED")
elif user_age < 0 or salary < 0 or req_loan < 0:
    print("Invalid")
else:
    print("APPROVED")
# # #-------------------------------------------
a = float(input())
b = float(input())
c = float(input())
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b and b == c:
                print("Equilateral")
            elif a != b:
                if b != c:
                    if a != c:
                        print("Isosceles")
            else:
                print("Scalene")
else:
    print("Does not exist")
# # #------------------------------------------------
# # #15
exam_score = int(input())
school_score = int(input())
age = int(input())
if exam_score <= 700 and exam_score >= 600:
    print("Scholarship")
elif exam_score >= 450 and exam_score < 600:
    print("Accepted")
elif exam_score >= 300 and exam_score < 450:
    if school_score >= 80:
        print("Accepted")
    else:
        print("Rejected")
elif exam_score < 300 and exam_score >= 0:
    print("Rejected")
else:
    print("Invalid")
# # #-------------------------------------------
# # #16
exam_score = int(input())
if exam_score < 0 or exam_score > 100:
    print("Invalid")
else:
    print("Pass") if exam_score >= 51 else print("Fail")
# #-------------------------------------------------
# #17
total = float(input())
mem_answer = input()
deliv_fee = 0
if total < 0:
    print("cant be negative")
elif mem_answer != "yes" or mem_answer != "no":
    print("only "yes" or "no"")
else:
    deliv_fee == 0 if total >= 50 or mem_answer == "yes" else deliv_fee == 5
print(deliv_fee , deliv_fee + total)
# #18
day = int(input())
match day:
    case 1:
        print("Mon")
        print("Study day")
    case 2:
        print("Tue")
        print("Study day")
    case 3:
        print("Wed")
        print("Study day")
    case 4:
        print("Thu")
        print("Study day")
    case 5:
        print("Fri")
        print("Study day")
    case 6:
        print("Sat")
    case 7:
        print("Sun")
    case _:
        print("Invalid")
# #----------------------------------
# # #19
print("T - tea , C - coffee , J - juice")
dr_code = input()
quant = int(input("Quantity: "))
match dr_code:
    case "T":
        price = 2
        total = price*quant
        print("Tea",quant, total)
        print("Large order") if total >= 20 else print("Regular")
    case "C":
        price = 4
        total = price*quant
        print("Coffee",quant, total)
        print("Large order") if total >= 20 else print("Regular")        
    case "J":
        price = 3
        total = price*quant
        print("Juice",quant, total)
        print("Large order") if total >= 20 else print("Regular")
    case _:
        print("Invalid")
# #--------------------------------------------------------
#20
student_id = input()
length = len(student_id)
if student_id.isdecimal() == False:
    print("Rejected, it must contain only 0,1,2,...,9  and no spaces")
elif student_id.isascii() == False:
    print("Rejected, it must only contain ascii charachters")
elif length != 8:
    print("Rejected, it must contain 8 letters")
else:
    print("Accepted")
# #---------------------------------------------
# #21
real_pin = "0427"
user_pin = input()
length = len(user_pin)
if length != 4:
    print("PIN must be 4 charachters")
elif user_pin.isascii() == False:
    print("PIN must have 4 ascii digits")
elif user_pin.isdecimal() == False:
    print("Only digits are allowed")
elif user_pin != real_pin:
    print("Incorrect PIN")
else:
    print("Access granted")
# #-------------------------------------------
#22
phone_number = input()
pref = phone_number[:3]
length = len(phone_number)

if phone_number.isascii() == False:
    print("It must contain only ascii characters")
elif phone_number.isdecimal() == False:
    print("Only ascii digits are allowed")
elif length != 10:
    print("it must contain 10 letters")
else:
    match pref:
        case "050":
            print("Accepted")
        case "051":
            print("Accepted")
        case "055":
            print("Accepted")
        case "070":
            print("Accepted")
        case "077":
            print("Accepted")
        case "099":
            print("Accepted")
        case _:
            print("It can only start with 050,051,055,070,077,099")
# # #----------------------------------------------------------------
# #23
# balance = 1000
# real_pin = "0427"
# user_pin = input()
# if user_pin.isascii() == False:
#     print("Only ascii")
# elif user_pin.isdecimal() == False:
#     print("Only decimal")
# elif len(user_pin) != 4:
#     print("it must be 4 letters")
# elif user_pin != real_pin:
#     print("Incorrect PIN")
# else:
#     print("PIN accepted")
#     withdraw_amount = input()
#     if withdraw_amount.isascii() == False:
#         print("only ascii")
#     elif withdraw_amount.isdecimal() == False:
#         print("Only digits")
#     elif len(withdraw_amount) == 0:
#         print("it cant be empty")
#     elif int(withdraw_amount) < 10 or int(withdraw_amount) > 500 or int(withdraw_amount)%10 != 0:
#         print("The amount must be between 10 and 500 AZN inclusive and divisible by 10.")
#     else:





#24
print("K - keyboard , M - mouse , H - headphones")
prod_code = input()
deliv_fee = 0



match prod_code:
    case "K":
        quant = input("Quantity: ")
        quanlen = len(quant) 
        subtotal = 40*int(quant)
        if quant.isascii() == False:
            print("Only ascii")
        elif quant.isdecimal() == False:
            print("only digits")
        elif int(quant) < 1 or int(quant) > 5:
            print(" It must be [1;5]")
        elif quanlen == 0:
            print("It cant be empty")
        else:
            coupon_code = input("Coupon: ")
            match coupon_code:
                case "NONE":
                    endirim = 0
                case "SAVE10":
                    if subtotal >= 100:
                        endirim = 10
                    else:
                        endirim = 0
                case _:
                    print("Invalid")
            disc_total = subtotal * (100 - endirim) / 100
            print("Delivery --> P (pickup) , S (standart)")
            deliv_code = input()
            match deliv_code:
                case "P":
                    deliv_fee == 0
                case "S":
                    deliv_fee == 0 if subtotal >= 80 else deliv_fee == 5
                case _:
                    print("Invalid")
    case "M":
        quant = input("Quantity: ")
        quanlen = len(quant) 
        subtotal = 20*int(quant)
        if quant.isascii() == False:
            print("Only ascii")
        elif quant.isdecimal() == False:
            print("only digits")
        elif int(quant) < 1 or int(quant) > 5:
            print(" It must be [1;5]")
        elif quanlen == 0:
            print("It cant be empty")
        else:
            coupon_code = input("Coupon: ")
            match coupon_code:
                case "NONE":
                    endirim = 0
                case "SAVE10":
                    if subtotal >= 100:
                        endirim = 10
                    else:
                        endirim = 0
                case _:
                    print("Invalid")
            disc_total = subtotal * (100 - endirim) / 100
            print("Delivery --> P (pickup) , S (standart)")
            deliv_code = input()
            match deliv_code:
                case "P":
                    deliv_fee == 0
                case "S":
                    deliv_fee == 0 if total >= 80 else deliv_fee == 5
                case _:
                    print("Invalid")
    case "H":
        quant = input("Quantity: ")
        quanlen = len(quant) 
        subtotal = 20*int(quant)
        if quant.isascii() == False:
            print("Only ascii")
        elif quant.isdecimal() == False:
            print("only digits")
        elif int(quant) < 1 or int(quant) > 5:
            print(" It must be [1;5]")
        elif quanlen == 0:
            print("It cant be empty")
        else:
            coupon_code = input("Coupon: ")
            match coupon_code:
                case "NONE":
                    endirim = 0
                case "SAVE10":
                    if subtotal >= 100:
                        endirim = 10
                    else:
                        endirim = 0
                case _:
                    print("Invalid")
            disc_total = subtotal * (100 - endirim) / 100
            print("Delivery --> P (pickup) , S (standart)")
            deliv_code = input()
            match deliv_code:
                case "P":
                    deliv_fee == 0
                case "S":
                    deliv_fee == 0 if total >= 80 else deliv_fee == 5
                case _:
                    print("Invalid")


total = disc_total + deliv_fee
if prod_code == "K":
    print("keyboard" , quant , subtotal , endirim,"%", deliv_fee , total)
elif prod_code == "M":
    print("mouse" , quant , subtotal , endirim,"%", deliv_fee , total)
elif prod_code == "H":
    print("headphone" , quant , subtotal , endirim,"%", deliv_fee , total)
else:
    print("Invalid")
#------------------------------------------------------------------------
student_id = input()
student_age = input()


length = len(student_id)
if student_id.isascii() == False:
    print("only ascii")
elif length != 8:
    print("it must be 8 characters")
elif student_id.isdecimal() == False:
    print("only decimal")
else:
    if int(student_age) < 16 or int(student_age) > 65:
        print("Restricted")
    else:
        if student_age.isascii() == False:
            print("only ascii")
        elif student_age.isdecimal() == False:
            print("only decimal")
        else:
            student_age = int(student_age)
            print("PY , WEB , CY")
            workshop_code = input()
            match workshop_code:
                case "PY":
                    if student_age < 16:
                        print("rejected")
                    else:
                        if student_age <= 18 and student_age >= 16:
                            discount = 20
                        else:
                            discount = 0
                    payment_amount = input()
                    if payment_amount.isascii() == False:
                        print("only ascii")
                    elif len(payment_amount) == 0:
                        print("it cant be empty")
                    elif payment_amount.isdecimal() == False:
                        print("ONly decimal")
                    else:

                case "WEB":
                    if student_age < 16:
                        print("rejected")
                    else:
                        if student_age <= 18 and student_age >= 16:
                            discount = 20
                        else:
                            discount = 0
                case "CY":
                    if student_age < 18:
                        print("rejected")
                    else:
                        if student_age <= 18 and student_age >= 16:
                            discount = 20
                        else:
                            discount = 0
                            

                












































#25
student_id = input()
student_age = input()
workshop_code = input()
payment_amount = input()

