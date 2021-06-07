myfile= open("fruits.txt")
file= myfile.read()
file= file.splitlines()
for i in file:
    print(len(i))
    
