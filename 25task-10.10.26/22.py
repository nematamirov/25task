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