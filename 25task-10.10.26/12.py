distance = float(input())
start_fee = 2
if distance >= 0 and <= 5:
    dist_fee = 0.70
    print(start_fee)
    print(dist_fee)
    print(start_fee + dist_fee*distance)
elif distance > 5 and <= 15:
    dist_fee = 0.60
    print(start_fee)
    print(dist_fee)
    print(start_fee + dist_fee*distance)
elif distance > 15:
    dist_fee = 0.50
    print(start_fee)
    print(dist_fee)
    print(start_fee + dist_fee*distance)
else:
    print("Invalid")