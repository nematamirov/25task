vote = input()
a_votes = 0
b_votes = 0
c_votes = 0
spoiled_votes = 0
while vote != "end":
    match vote:
        case "A":
            a_votes = a_votes + 1
        case "B":
            b_votes = b_votes + 1
        case "C":
            c_votes = c_votes + 1
        case _:
            spoiled_votes = spoiled_votes + 1
    vote = input()
print("A:",a_votes,"B:",b_votes,"C:",c_votes)
print("Spoiled: ",spoiled_votes)

if a_votes > b_votes and a_votes > c_votes:
    print("Winner: A")
elif b_votes > a_votes and b_votes > c_votes:
    print("Winner: B")
elif c_votes > a_votes and c_votes > b_votes:
    print("winner : C")
else:
    print("tie")
