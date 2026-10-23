user_pass = input()
digit_count = 0
upper_count = 0
lower_count = 0
for i in user_pass:
    if i.isdigit() == True:
        digit_count += 1
    if i.isupper() == True:
        upper_count += 1
    elif i.islower() == True:
        lower_count += 1
if len(user_pass) >= 8:
    if digit_count >= 1:
        if upper_count >= 1:
            if lower_count >= 1:
                print("Strong pass")
            else:
                print("weak . at least 1 lower characters")
        else:
            print("at least 1 upper character")
    else:
        print("weak, must have at least 1 digit")
else:
    print("Weak pass, it must be at least 8 characters")