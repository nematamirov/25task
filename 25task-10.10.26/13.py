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