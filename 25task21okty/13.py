hot = 0
temp = float(input("Day 1: "))
max = temp
for i in range (1 , 8):
    if temp > 30:
        hot = hot + 1
    if temp > max:
        max = temp
    temp = float(input())
print("Hot days: ",hot,"Hottest day: ",max )