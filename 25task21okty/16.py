save = 50
total = 50
i = 1
while total <= 1000:
    print("Month",i,total)
    i = i + 1
    save = save + 10
    total = total + save
print("Month", i , total)
print("Goal reached in",i,"month")