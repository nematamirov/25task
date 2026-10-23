adult_ticket = 0
child_ticket = 0
for i in range (1 , 6):
    user_age = int(input("Age of visitor: "))
    if user_age < 18:
        child_ticket = child_ticket + 1
    else:
        adult_ticket = adult_ticket + 1
print(child_ticket , adult_ticket)