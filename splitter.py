from __future__ import division  
import fileinput
import numpy as np
import matplotlib.pyplot as plt


with open('fort.83','r') as f:
    lines = f.read().split("\n")


print("Number of lines is {}".format(len(lines)))
j=0
i=0
for i,line in enumerate(lines):
	finded = line.find('BEGIN')
        if finded != -1 and finded != 0:
            j += 1   
f.close()
print  'How many files to be created?',j

vec=[]
count=0
with open('fort.83','r') as f: 
	for i, line in enumerate(f): 
		if line.startswith(' ## BEGIN'): 
			count += 1
			vec.append(' ## BEGIN',)
		elif line.startswith(' ## END'): 
			vec.append(' ## END') 
			np.savetxt('hrd%d.txt'%(count),vec,fmt='%s')
			vec=[]
		else: vec.append(line)
f.close()	




