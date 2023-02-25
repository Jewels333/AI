# Enrichment Boat Simulation
# Jewels, Yusuf 
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
                return line
class api:
    dataFile = 'programs/environment4/data'
    envFile = 'programs/environment4/env'
    boatFile = 'programs/environment4/boat'
    class data:
        connection = open(dataFile)
        content = connection.read()
        with content as data: #to READ the DATA
            pass
    class env:
        connection = open(envFile)
        content = connection.read()
        with content as environment: #to CREATE the ENVIORMENT
            pass
    class boat:
        connection = open(boatFile)
        content = connection.read()
        with content as boat: #to CREATE the BOAT
            pass
    