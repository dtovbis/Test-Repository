#This line returns a list of unique words in a file.
fname=input("Enter file: ")
fhand=open(fname)
uniquewords=[]
for line in fhand:
    spl=line.rstrip()
    spl=line.split()
    for word in spl:
        if word not in uniquewords:
            uniquewords.append(word)
uniquewords.sort()
print(uniquewords)