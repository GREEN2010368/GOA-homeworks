products=["apple", "banana", "milk", "bread", "chocolate"]
print("product list:")
print(products)
index=int(input("enter product index: "))
if 0<=index<len(products):
    print(products[index])