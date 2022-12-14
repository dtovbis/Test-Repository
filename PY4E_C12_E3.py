#This script imports a file and displays the first 3000 characters using urllib instead of a socket.
import urllib.request
url = input('Enter a URL: ')
try:
    fhand = urllib.request.urlopen(url)
except:
    print('Invalid or improperly formatted URL')
    quit()
print(fhand.read(3000).decode().strip())
print('Full file contains', len(fhand.read()), 'Characters')