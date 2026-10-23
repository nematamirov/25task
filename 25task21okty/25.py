card_no = input()


add_up = 0
while len(card_no) != 16:
    if len(card_no) != 16:
        print("must be 16 digits")
    card_no = input()
     

if card_no.isdecimal() == False:
    print("only digits")
elif card_no.isascii() == False:
    print("only ascii")
else:
    card_no_rev = card_no[::-1]
    for i in range (1 , 16):
        if i % 2 == 0:
            a = int(card_no_rev[i]) * 2
            if a > 9:
                a = a - 9
                add_up = add_up + a
        add_up = add_up + int(card_no_rev[i])
if add_up % 10 == 0:
    print("valid")
else:
    print("invalid")
    
