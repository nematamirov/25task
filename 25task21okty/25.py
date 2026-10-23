card_no = input()
while len(card_no) != 16:
    print("Must be 16 digits")
    card_no = input()
add_up = 0
card_no_rev = card_no[::-1]
for i in range(0 , 16):
    digit = int(card_no_rev[i])
    if i % 2 == 1:
        digit = digit * 2
        if digit > 9:
            digit = digit - 9
    add_up = add_up + digit

if add_up % 10 == 0:
    print("valid")
else:
    print("invalid")