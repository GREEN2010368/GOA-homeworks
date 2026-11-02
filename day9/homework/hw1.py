user_age=int(input("please enter your age: "))
if user_age < 0:
    print("invalid age")
elif user_age >= 18:
    print("Adult")
else:
    print("minor")