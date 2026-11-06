raodenoba=int(input("please raodenoba: "))
total=0
for i in range(raodenoba):
    cost=float(input("please enter cost of the product"))
    total+=cost
if total>200:
    total=total-total*0.15
elif total>=100:
    total=total-total*0.10
print(total)