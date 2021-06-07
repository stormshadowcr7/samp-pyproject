
number=[1,2,3]
file= open("sample.txt","w")
for i in number:
    file.write(str(i)+ "\n")
file=file.close()
