def find(fp, word):
    
    with open(fp, 'r') as fp:
        # read all lines in a list
       lines = fp.readlines()
       for line in lines:
         # check if string present on a current line
         if line.find(word) != -1:
                print(word, 'string exists in file')
                print('Line Number:', lines.index(line))
                print('Line:', line)
class api:
    dataFile = 'programs/environment4/data'
    envFile = 'programs/environment4/env'
    boatFile = 'programs/environment4/boat'
    class data:
        connection = open(dataFile)
    class env:
        connection = open(envFile)
    class boat:
        connection = open(boatFile)
    