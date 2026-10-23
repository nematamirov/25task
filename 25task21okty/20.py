total = 0

for i in range (2 , 101):
    bolen_say = 0
    for j in range(1 , i+1):
        if i % j == 0:
            bolen_say = bolen_say + 1
    if bolen_say == 2:
        print(i)
        total = total + 1
        print(total)
        