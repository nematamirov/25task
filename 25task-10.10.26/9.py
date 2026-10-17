a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
    smallest = a
    if a > b and a > c:
        biggest = a
    elif b > a and b > c:
        biggest = b
        mid = c
    else:
        biggest = c
        mid = b
elif b < a and b < c:
    smallest = b
    if a > b and a > c:
        biggest = a
        mid = c
    elif b > a and b > c:
        biggest = b
    else:
        biggest = c
        mid = a
else:
    smallest = c
    if a > b and a > c:
        biggest = a
        mid = b
    elif b > a and b > c:
        biggest = b
        mid = a
    else:
        biggest = c
print(smallest, mid , biggest)

