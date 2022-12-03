str = 'X-DSPAM-Confidence:0.8475'
colonpos= str.find(':')
value=float(str[colonpos+1:])
print(value)
