age=int(input("please enter your age"))
score=int(input("please eneter your score"))
if age > 18 and score >= 70:
    print("you pass")
elif age < 18 and score >= 70:
    print("good result but you are under 18")
elif score < 70:
    print("failed")