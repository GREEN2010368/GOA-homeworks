start=int(input("please enter your first number "))
end=int(input("please enter your last number"))
while start <= end:
    if start > 0 and start % 2 == 0:
        print("positive even")
else:
    print("start")
start += 1