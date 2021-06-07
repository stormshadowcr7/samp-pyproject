import glob2
from datetime import datetime
file= glob2.glob("*.txt")
with open(datetime.now().strftime("%y-%m-%d-%H-%M-%S-%f")+ ".txt", "w") as doc:
    for i in file:
        with open(i, "r") as text:
            doc.write(text.read()+ "\n")
        
        
