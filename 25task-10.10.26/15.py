exam_score = int(input())
school_score = int(input())
age = int(input())
if exam_score <= 700 and exam_score >= 600:
    print("Scholarship")
elif exam_score >= 450 and exam_score < 600:
    print("Accepted")
elif exam_score >= 300 and exam_score < 450:
    if school_score >= 80:
        print("Accepted")
    else:
        print("Rejected")
elif exam_score < 300 and exam_score >= 0:
    print("Rejected")
else:
    print("Invalid")