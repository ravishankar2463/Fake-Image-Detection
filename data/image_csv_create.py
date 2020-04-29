import os
currentDirectory = os.getcwd()

file1 = open("MyFile.txt","w") 
# r=root, d=directories, f = files
for r, d, f in os.walk(currentDirectory):	
	for file in f:
		if ("real" in r):
			str1=str(os.path.join(r, file)+",0\n")
			file1.write(str1)
		else:
			str2=str(os.path.join(r, file)+",1\n")
			file1.write(str2)

file1.close()