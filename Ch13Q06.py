#(Count words) Write a program that counts the number of words in President
#Abraham Lincolns Gettysburg Address from http://cs.armstrong.edu/liang/data/
#Lincoln.txt. 

import urllib.request

file = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
content = file.read()
print(str(len(content.split())) + " words") 