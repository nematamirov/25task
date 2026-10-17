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