#This script calculates the average of a list of numbers.
numarray=[]
i=0
while True:
    numarray.append(input('Enter A Number: '))
    if numarray[i] == 'done':
        numarray.pop()
        break
    try:    
        numarray[i]=float(numarray[i])
        i=i+1
    except:
        print('Invalid Input')
        numarray.pop()
res=[sum(numarray), len(numarray),sum(numarray)/len(numarray)]
print(res)
res2=[max(numarray),min(numarray)]
print(res2)