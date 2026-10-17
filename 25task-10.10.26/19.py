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