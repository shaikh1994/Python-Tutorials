import sys
import os

path = input("Enter the directory between testcase1 or testcase2: ")
fileName = []
fileValue = []
     
for root, dirs, files in os.walk(path):
	for file in files:
		if(file.endswith(".txt")):
			#print(os.path.join(root,file))
			a=os.path.join(root,file)
			#print(open(a,'r').readlines())
			b=open(a,'r').readlines()
			fileValue.append(int(b[0].strip()))
			c=file[0].split('.')
			#print(c)
			fileName.append(c[0])
			
sortedV=sorted(fileValue)
for i in sortedV:
    print(fileName[fileValue.index(i)])


