fname=input("Enter a file name: ")
fhand=open(fname)
emaildict= dict()
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        spl=line.split()
        emaildict[spl[1]]= emaildict.get(spl[1],0) +1
emaillist=list()
for key,val in list(emaildict.items()): #.items is a set of tuples containing the items in the dictionary
    #So we are creating a list of tuples from the dictionary, and appending those values in reverse order to a new list
    emaillist.append((val,key)) #Append the tuple, so an extra pair of brackets
emaillist.sort(reverse=True)
print(emaillist[0][1],emaillist[0][0])