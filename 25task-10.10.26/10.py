acc_balance = 1000
withdraw = float(input())
rem_balance = acc_balance - withdraw
if withdraw <= 0:
    print("Invalid amount")
elif rem_balance < 0:
    print("Insufficient balance")
else:
    print(rem_balance)