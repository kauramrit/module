#Q.1 print the current day using datetime module.

import datetime
now=datetime.datetime.now()
print("current day: %d" %now.day)

#Q.2 open your browser and play a video using webbrowser module in python.
import webbrowser
webbrowser.open('http://www.youtube.com/watch?v=9xVp8m0fJSg')

#Q.3 write a program to rename all the files in a directory and convert them into .jpg file format.

import os
path = 'C:/Users/AKUL/DC'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
    i = i+1
