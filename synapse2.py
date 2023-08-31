#task1
 
   
superheroes=['DocToR_sTRAngE','sPidERmaN','MoON_KnigHT','caPTAIN_aMERIca','hULK']
indices=[]
decoded_names=[]
name_length=[]




for i in range(0,5):  
    a=superheroes.index(superheroes[i])
    indices.append(a)
    s=superheroes[i].replace('_',' ').lower()
    decoded_names.append(s)


print(indices) 
print(decoded_names)

l=lambda x:len(x)
name_length=list(map(l,superheroes))
print(name_length)   

indices.sort(key=lambda x: name_length[x])

new = [decoded_names[i].title() for i in indices]


print("Phase 5 kick off list:")
for i, guest in enumerate(new, start=1):
    print(f"{i}. {guest}")


    
  
    
    

   