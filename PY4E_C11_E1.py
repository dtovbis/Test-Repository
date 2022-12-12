#This program shows the number of lines that matched the user-given regex in mbox.txt
import re
inp=input('Enter a regular expression: ')
lst=list()
hand = open('mbox.txt')
for line in hand:
    line=line.rstrip() #Strip trailing characters
    x=re.findall(inp,line) #Find inp in line
    if len(x) > 0 : lst.append(x) # If it found something, append the line to 'list'
print('mbox.txt had ', str(len(lst)), ' lines that matched ', inp) #Print the length of the list.