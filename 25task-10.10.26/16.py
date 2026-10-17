exam_score = int(input())
if exam_score < 0 or exam_score > 100:
    print("Invalid")
else:
    print("Pass") if exam_score >= 51 else print("Fail")