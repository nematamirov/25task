real_user = "admin"
real_pass = "1234"
chances = 3
wrong_attempt = 0
while wrong_attempt < 3:
    user = input("USer: ")
    pasw = input("Pass: ")
    if user == real_user and pasw == real_pass:
        print("Welcome")
        break
    else:
        wrong_attempt = wrong_attempt + 1
        if wrong_attempt == 3:
            print("account blocked")
        else:
            print("user or pass is wrong try again")
        