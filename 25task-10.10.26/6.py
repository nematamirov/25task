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
