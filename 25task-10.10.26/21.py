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