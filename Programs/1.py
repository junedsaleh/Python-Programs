i = input("Enter Number")
i = int(i)
j = 0
nm= []
l= []
for j in range(i):
    n=input("Enater Name")
    nm.append(n)
for j in nm:
    l.append(len(j))
    
print(nm)
print(l)
