temp = [10,-20,-289,100]
with open("file.txt" , "w")as myfile:
    for i in temp:
        if i>-273.15:
            f= i*9/5 +32
            myfile.write(str(f) +" \n")
           
