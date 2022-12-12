#This script returns a dictionary of senders and the number of emails they sent.
# If Splitdomains = Y, it groups by domain instead.
fname=input("Enter a file name: ")
isdomain=input("Split domains Y/N")
fhand=open(fname)
emaildict= dict()
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        spl=line.split()
        if isdomain == 'N':
            emaildict[spl[1]]= emaildict.get(spl[1],0) +1
        else: 
            emaildict[spl[1].split("@")[1]]= emaildict.get(spl[1].split("@")[1],0) +1
# I understand how this works but it is less pretty
# mostemails= 0
# mostkey = []
# for key in emaildict:
#     if emaildict[key] > mostemails:
#         mostemails=emaildict[key]
#         mostkey=key
# print(mostkey,mostemails)
most_emails=max(emaildict, key=emaildict.get) #This line tells max to search over email dict, but instead of using the keys, use the value associated with that key
print(emaildict)
print(most_emails,emaildict.get(most_emails))
