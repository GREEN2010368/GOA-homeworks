dadebiti=0
uarkofiti=0
kenti=0
luwi=0
for i in range (10):
    number=int(input("please enter your number"))
    if number>0:
        dadebiti+=1
    if number<0:
        uarkofiti+=1
    if number % 2==0:
        luwi+=1
    else:
        kenti +=1