empty = 20
command = input()
while command != "stop":
    if command == "in":
        empty = empty - 1
        print(empty)
    elif command == "out":
        empty = empty + 1
        print(empty)
    else:
        print("unknown command")
    command = input()