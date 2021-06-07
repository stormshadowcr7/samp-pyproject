import glob2
from datetime import datetime

file= glob2.glob("*.txt")
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+ ".txt", "w") as myfile:
    for i in file:
        with open(i, "r") as doc:
            myfile.write(doc.read() + "\n")
    
    
