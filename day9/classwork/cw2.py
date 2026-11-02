score=int(input("please enter your score"))
if 90 < score < 100:
    print("A")
elif 80 < score < 90:
    print("B")
elif 70 < score < 80:
    print("C")
elif 50 < score < 70:
    print("E")
elif 0< score < 50:
    print("F")
else:
    print("fail")