# writing out first file:
myfile = open('myfile.txt', 'w') #create a file handle
myfile.write('Hello text file!')
myfile.write('Goodbye text file!')
myfile.close()

# a handle is like a tv remote control

# read from a file one line at the time:
myfile = open('myfile.txt', 'r') # open file for reading
while True:
    line = myfile.readline() # read the next line
    if len(line) == 0: # END OF FILE
        break
    print(line)
myfile.close()

# turning a file into a list of lines:
f = open('myfile.txt', 'r')
lines = f.readlines() # read the entire file into a list
f.close()
lines.sort()

g = open('sorted.txt', 'w')
for line in lines:
    g.write(line)
g.close()

# reading the whole file at once:
f = open('myfile.txt') # reading mode by default
data = f.read() # read the entire file into a string
f.close()
words = data.split() # split the string into a list of words
print(words)

# working with binary files:
f = open('binfile.rar', 'rb') # open for reading in binary mode
g = open('copyfile.rar', 'wb') # open for writing in binary mode
while True:
    buf = f.read(1024) # read 1024 bytes at a time
    if len(buf) == 0:
        break
    g.write(buf) # write the bytes to the new file
f.close()
g.close()

# directory:
wordsfile = open('C://Users//DELL//Desktop//learn-python-the-right-way//myfile.txt', 'r')
wordlist = wordsfile.readlines()
print(wordlist)

# fitching a file from the web:
import urllib.request
url = "https://www.itef.org/rfc/rfc959.txt"
destination = "rfc959.txt"
urllib.request.urlretrieve(url, destination) # download the file

# reteive the content and display it:

def reteive_page(url):
    """retrieve the contents of a web page and return it as a string"""
    my_socket = urllib.request.urlopen(url)
    my_str = str(my_socket.read())
    my_socket.close()
    return my_str
the_text = reteive_page("https://www.itef.org/rfc/rfc959.txt")
print(the_text)
