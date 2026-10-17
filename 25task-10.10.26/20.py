student_id = input()
length = len(student_id)
if student_id.isdecimal() == False:
    print("Rejected, it must contain only 0,1,2,...,9  and no spaces")
elif student_id.isascii() == False:
    print("Rejected, it must only contain ascii charachters")
elif length != 8:
    print("Rejected, it must contain 8 letters")
else:
    print("Accepted")