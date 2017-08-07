import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

lenA = len(a)
lenB = len(b)
maxOfAB = max(lenA,lenB)
#one method
for i in range(maxOfAB):
    for n in range(len(a)):
        if b[i] == a[n]:
            c.append(b[i])           
print(c)
#changing list to set
d = set(c)
print(d)

# another method
d=[]
for i in range(maxOfAB):
   if b[i] in a:
       d.append(b[i])
print(d)
       

#generating random list
number=[]
for n in range(11):
    number.append(random.randint(0,100))
print(number)
    
        
        
