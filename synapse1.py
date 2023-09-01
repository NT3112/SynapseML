import random
lst=[]
new_lst=[]

a=int(input("Enter the no of elements in the list"))
for i in range(0,a):
    e=input()
    lst.append(e)
print(lst)
for j in range(0,a):
    decimal=int(lst[j],2)
    new_lst.append(decimal)
print(str(new_lst))  

for i in range(0,100):
    if(len(new_lst)>2):
        a=random.choice(new_lst)
        new_lst.remove(a)
        b=random.choice(new_lst)
        new_lst.remove(b)
        c=a+b
        new_lst.append(c)
        print(new_lst)
    else:
        break     

print(new_lst)




