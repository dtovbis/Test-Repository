#This program searches for lines of the form "new revision: 12345"
#It then extracts the number and calculates the average.
import re
inp=input('Enter file: ')
lst=[]
hand = open(inp)
strtofind='^New Revision: ([0-9]+)' #Define the regex
for line in hand:
    line=line.rstrip() #Strip trailing characters
    x=re.findall(strtofind,line) #Find inp in line
    if len(x) > 0 : lst.append(float(x[0])) # If it found something, append the line to 'list'
    #Note we assume that there is only one matching string per line(which in our case there should be)
print(int(sum(lst)/len(lst)))