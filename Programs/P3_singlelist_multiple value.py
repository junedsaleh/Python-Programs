##n = int(input("Enter Number"))
i = 0
name = ["Akib","Amir"]
city = ["Bharuch","Ankleshwar"]
mobile = [9723,6352]
lst = [name,city,mobile]

##while(i<n):
##    nm= input("Enter Name")
##    name.append(nm)
##    ct= input("Enter City")
##    city.append(ct)
##    mn= input("Enter MN")
##    mobile.append(mn)
##    i = i+1
##print(lst)

s = input("Enter City")
for i in lst[1]:
    if(i==s):
        print(lst)
