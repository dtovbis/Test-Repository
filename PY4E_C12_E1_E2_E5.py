#This script loads a file from a URL and displays the first 3000 characters of the file (after the header) using sockets.
import socket
import re
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter a URL: ')
try:
    urlsp = url.split("/")
    dmn=urlsp[2]
    mysock.connect((dmn, 80))
except:
    print('Invalid or improperly formatted URL')
    quit()
cmdstr = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
print(cmdstr)
cmd =cmdstr.encode()
mysock.send(cmd)
numchars=0
document=''
strtofind='\n\n((.|\n)*)' #Find two newlines which siginifies the end of the header then extract everything after the newlines
while True:
    data = mysock.recv(512)
    numchars += len(data)
    if len(data) < 1:
        break
    document += data.decode().strip()
    #print(data.decode(),end='')
noheaders=re.search(strtofind,document)
print(noheaders.group(0)[:3000])
print('\n Total Length:', numchars, 'Characters')
mysock.close() 
