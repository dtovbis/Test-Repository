#This program calculates letter frequency in a text file.
fname=input("Enter a file name: ")
fhand=open(fname)
letterdict=dict.fromkeys(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],0)
for line in fhand:
    line=line.lower()
    words=line.split()
    for word in words:
        for letter in word:
            if letter in letterdict:
                letterdict[letter]= letterdict.get(letter,0) +1
letterlist=list(letterdict.items())
letterlist.sort()
totalletters=sum(j for i, j in letterlist)
for key,val in letterlist:
    print(key/totalletters*100)