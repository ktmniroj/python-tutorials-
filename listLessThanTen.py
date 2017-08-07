list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList =[]
for num in list:
    if num<5:
        newList.append(num)
    
print(newList)
secList=[]
n = int(input("enter any number"))
for num in list:
    if num<n:
        secList.append(num)
print(secList)
