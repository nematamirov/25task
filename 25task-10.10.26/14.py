a = float(input())
b = float(input())
c = float(input())
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b and b == c:
                print("Equilateral")
            elif a != b:
                if b != c:
                    if a != c:
                        print("Isosceles")
            else:
                print("Scalene")
else:
    print("Does not exist")