total = float(input())
mem_answer = input()
deliv_fee = 0
if total < 0:
    print("cant be negative")
elif mem_answer != "yes" or mem_answer != "no":
    print("only "yes" or "no"")
else:
    deliv_fee == 0 if total >= 50 or mem_answer == "yes" else deliv_fee == 5
print(deliv_fee , deliv_fee + total)