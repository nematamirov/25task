for i in range (1 , 6):
    if i == 4:
        continue
    print("Floor",i, end= " ")
    for j in range (1 , 5):
        print(i*100 + j , end = " ")
    print()        