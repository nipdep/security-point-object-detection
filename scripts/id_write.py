
import os

with open('./ids.txt','w') as pf:
    print(1)
    for root, dirs, files in os.walk("./data/Images/Labels"):
        for filename in files:
            print(filename)
            pf.write(filename+"\n")
        
print(2)
