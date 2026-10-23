balance = 500
i = 1
while True:
    draw = float(input())
    if draw == 0:
        print("Goodbye")
        break
    elif draw < 0:
        print("Invalid amount")
    elif draw > balance:
        print("INsufficent")
    else:
        balance = balance - draw
        print(balance)