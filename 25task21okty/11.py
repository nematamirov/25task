grade = float(input("Grade: "))
pass_amount = 0
fail_amount = 0
max = grade
counter = 1
sum = grade
while grade != -1:
    if grade >= 51:
        pass_amount = pass_amount + 1
    else:
        fail_amount = fail_amount + 1
    if grade > max:
        max = grade
    grade = float(input("Grade: "))
    counter = counter + 1
    sum = sum + grade
print(pass_amount,fail_amount,max , sum/counter)