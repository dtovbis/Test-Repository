fname=input("Enter file: ")
fhand=open(fname)
emaillist=[]
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        print(line)
        spl=line.split()
        # if spl[1] not in emaillist:
        emaillist.append(spl[1])
print('There were ' , len(emaillist) , ' lines in the file with From as the first word')
