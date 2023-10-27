import os.path
#import OS.path (case sensitive) 
path = 'gpa.txt'

checkFile = os.path.isfile(path)

if checkFile == True:
#needs two = sign 
    infile = open(path, 'r')
#in.file is incorrect 
    outputFile = infile.read()
    print(outputFile)
#print #outputfile
else:
#else 
    print('file does not exist')
#missing quotation mark at the end. ('file does not exist) 
