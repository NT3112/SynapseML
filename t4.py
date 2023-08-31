

def explode_chains():
    encoded_lists=[[1,2,3,4,6],[5,7,8,9,15],[12,14,16,18],[10,11,12,13,16,17,18,20]]
    for i in range(0,4):
        for j in range (0,len(encoded_lists[i])):
           
           if(j<len(encoded_lists[i])-2):
                
                  if(encoded_lists[i][j]+1==encoded_lists[i][j+1] and encoded_lists[i][j]+2==encoded_lists[i][j+2]  ):

                    encoded_lists[i][j]=100
                    encoded_lists[i][j+1]=100
                    encoded_lists[i][j+2]=100

    element_to_remove = 100


    cleaned_list = [[value for value in sublist if value != element_to_remove] for sublist in encoded_lists]

    print(cleaned_list)        

         

explode_chains()     
    

                  
                
                  
                  
            
 

