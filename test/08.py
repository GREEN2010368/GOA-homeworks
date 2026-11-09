n=int(input("please enter n: "))
first=True
previous_number=-1
while n>0:
    number=n%10
    if previous_number !=-1:
        if number%2==previous_number %2:
            first=False
previous_number=number
n=n//10
print(first)