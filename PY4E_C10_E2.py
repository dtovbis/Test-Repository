fname=input("Enter a file name: ")
fhand=open(fname)
timedict=dict()
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        spl=line.split()
        time=spl[5].split(":")
        timedict[time[0]]= timedict.get(time[0],0) +1
timelist=list(timedict.items())
timelist.sort()
for key,val in timelist:
    print(key,val)