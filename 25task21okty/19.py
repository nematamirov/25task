total = 0.0
while total < 1.5:
    coin = float(input())
    if coin == 0.05 or coin == 0.1 or coin == 0.2 or coin == 0.5 or coin == 1.0:
        total = total + coin
        print(total)
    else:
        print("not accepted")
print("here is your water")
print(total - 1.5)