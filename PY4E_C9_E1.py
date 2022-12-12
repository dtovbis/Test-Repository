#This returns if a particular word is found in a text file
fhand=open('words.txt')
merweb= {}
for line in fhand:
    words=line.split()
    for word in words:
        merweb[word]=len(word)
print('newfound' in merweb)
print('Obama' in merweb)
print('computers' in merweb)