import os
# Python File Modes
# Mode	Description
# 'r'	Open a file for reading. (default)
# 'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
# 'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# 't'	Open in text mode. (default)
# 'b'	Open in binary mode.
# '+'	Open a file for updating (reading and writing)

# Python File Methods
# Method	Description
# close()	Close an open file. It has no effect if the file is already closed.
# detach()	Separate the underlying binary buffer from the TextIOBase and return it.
# fileno()	Return an integer number (file descriptor) of the file.
# flush()	Flush the write buffer of the file stream.
# isatty()	Return True if the file stream is interactive.
# read(n)	Read atmost n characters form the file. Reads till end of file if it is negative or None.
# readable()	Returns True if the file stream can be read from.
# readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
# readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
# seekable()	Returns True if the file stream supports random access.
# tell()	Returns the current file location.
# truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
# writable()	Returns True if the file stream can be written to.
# write(s)	Write string s to the file and return the number of characters written.
# writelines(lines)	Write a list of lines to the file.
with open("S:\\python programme\\sampletest.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\\n")
   f.write("This file\\n\\n")
   f.write("contains three lines\\n")
   f.write("contains Fourth lines\\n")
f.close()

f = open("S:\\python programme\\sampletest.txt",mode = 'r',encoding = 'utf-8')
#print(f.readlines())
print(f.readline())
#print(f.read())
f.close()

print(os.getcwd())
#dir = os.chdir('C:\\Users\\SANKAR\\Downloads\\python-3.7.4-embed-amd64')
#print(dir)
os.mkdir('test')
os.mkdir('test2')
print(os.listdir())
os.rename('test','new_one')
os.rmdir('new_one')
import shutil
shutil.rmtree('test2')
os.listdir()

import csv
with open('people.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
csvFile.close()
#CSV Files with quotes
#We can write the csv file with quotes, by registering new dialects using 
# csv.register_dialect() class of csv module
csv.register_dialect('myDialect',
delimiter = ',',
skipinitialspace=True)
with open('people.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for row in reader:
        print(row)
csvFile.close()

#Example 1: Modifying existing rows of people.csv

row = ['3', ' Marie', ' California']
with open('people.csv', 'r') as readFile:
 reader = csv.reader(readFile)
 lines = list(reader)
 lines[2] = row
 
with open('people.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
readFile.close()
writeFile.close()

row = ['4', ' Danny', ' New York']
with open('people1.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)
csvFile.close()

