pass_leng = 0
while pass_leng < 8:
    passwrd = input()
    pass_leng = len(passwrd)
    if pass_leng < 8:
        print("too short try again")
    else:
        break
print("Pass accepted")
