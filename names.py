f = open("testList.txt", "w") 

import glob, os
os.chdir("./test")
for file in glob.glob("*.txt"):
    f.write("000/" + str(file)+"\n") 
    
f.close()