bolen = 0
total = 0
for i in range (2, 101):
    for j in range (1 , i+1):
        if i%j == 0:
            bolen = bolen + 1
    if bolen <= 2:
        print(i)
        total = total + 1
    
