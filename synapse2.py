#task1
 
   
superheroes=['DocToR_sTRAngE','sPidERmaN','MoON_KnigHT','caPTAIN_aMERIca','hULK']
indices=[]
decoded_names=[]
name_length=[]




for i,n in enumerate(superheroes): 
    indices.append(i)
    decoded_names.append(n.replace('_',' ').lower())



print(indices) 
print(decoded_names)

l=lambda x:len(x)
name_length=list(map(l,superheroes))
print(name_length)

indices.sort(key=lambda x:name_length[x])
new = [decoded_names[i].title() for i in indices]


print("Phase 5 kick off list:")
for i, guest in enumerate(new, start=1):
    print(f"{i}. {guest}")


    
  
    
    

   