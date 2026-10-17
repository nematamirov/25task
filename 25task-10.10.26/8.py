org_price = float(input())
if org_price < 100:
    disc_amount = 0
    print(org_price)
    print(disc_amount)
    print(org_price*(100-disc_amount)/100)
elif org_price >= 100 and org_price < 300:
    disc_amount = 10
    print(org_price)
    print(disc_amount)
    print(org_price*(100-disc_amount)/100)
elif org_price >= 300 and org_price < 500:
    disc_amount = 15
    print(org_price)
    print(disc_amount)
    print(org_price*(100-disc_amount)/100)
elif org_price >= 500:
    disc_amount = 20
    print(org_price)
    print(disc_amount)
    print(org_price*(100-disc_amount)/100)
else:
    print("Invalid input")