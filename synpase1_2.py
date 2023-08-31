import random
lst=['0001','0011','0101','1011','1101','1111']
new_lst=[]
for j in range(0,6):
    decimal=int(lst[j],2)
    new_lst.append(decimal)
print(str(new_lst))
while(len(new_lst)>2):
    new_lst.sort()
    smallest = new_lst.pop(0)  
    second= new_lst.pop(0)   
    sum = smallest + second 
    new_lst.append(sum) 

print(new_lst)    
