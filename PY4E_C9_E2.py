fname=input("Enter a file name: ")
fhand=open(fname)
emaildict= dict()
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        spl=line.split()
        emaildict[spl[2]]= emaildict.get(spl[2],0) +1
print(emaildict)