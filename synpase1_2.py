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

while(len(new_lst)>2):
    new_lst.sort()
    a = new_lst.pop(0)  
    b= new_lst.pop(0)   
    sum = a+b
    new_lst.append(sum) 

print(new_lst)    
