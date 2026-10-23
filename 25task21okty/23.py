left_mins = 480
i = 1
serv_num = 0
while left_mins > 0:
    need = int(input())
    if need > left_mins:
        print("sorry come back tmrw")
        
        
        break
    elif need == 0:
        break
    else:
        left_mins = left_mins - need
        serv_num = serv_num + 1
    i = i + 1
print("Customers served: ",serv_num)
print("Mins left: ",left_mins)