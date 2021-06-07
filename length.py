myfile= input("enter a string = ")
def length(l):
    if type(myfile)==int:
        return("int ka lenth nhi hota chu")
    else:    
        return(len(l))
print(length(myfile))
    
