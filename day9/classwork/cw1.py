age=int(input("please enter your age"))
if 0 < age < 12:
    print("user is young")
elif 12 < age < 18:
    print("user is teen")
elif 18 < age < 60:
    print("user is adult")
elif 60 < age < 100:
    print("user is old")
else:
    print("leave")