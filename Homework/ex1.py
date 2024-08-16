fruites = ["banana" , "mango" , "apple" , "orange"]
result=""
for i in range(len(fruites)):
    if i ==len(fruites)-1:
        result+=str(len(fruites[i]))
    else:
         result+=str(len(fruites[i])) +"-"
print(result)
        
    

