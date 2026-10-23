user_pass = input()
dig_count = 0
up_count = 0
low_count = 0
for i in user_pass:
    if i.isdigit() == True:
        dig_count = dig_count + 1
    elif i.isupper() == True:
        up_count = up_count + 1
    elif i.islower() == True:
        low_count = low_count + 1
if len(user_pass) >= 8 and dig_count >= 1 and up_count >= 1 and low_count >= 1:
    print("Strong password")
elif         