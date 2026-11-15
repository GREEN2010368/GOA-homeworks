word=input("please enter a word: ")
count=0
for i in word:
    if i in "aeiouAEIOU":
        count+=1
print(count)