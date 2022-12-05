fname=input('Enter a file name:')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    quit()
try:
    fhand=open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
value = 0
for line in fhand:
    line=line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        colonpos= line.find(':')
        value= value + float(line[colonpos+1:])
        count = count +1
print('Average Spam Confidence:', value/count)