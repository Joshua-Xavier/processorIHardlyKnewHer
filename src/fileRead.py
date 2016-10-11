'''
AUTHOR: Joshua Nelsson-Smith
STUDENT ID: 25954113
START DATE: 11/10/16
LAST MODIFIED: 11/10/16
DESCRIPTION: This file handles the parsing of a processes.txt file found in an
input directory. It scans through the text file and returns an array of process
elements where:
    index[0] = process name
    index[1] = process arival time
    index[2] = process duration
'''

def getData(filePath):
    f = open(filePath, 'r')
    processArray = []
    for line in f:
        currentItem = line.split()
        processArray.append(currentItem)
    f.close()
    return processArray


'''
testArray = getData()
for item in testArray:
    print(item)
'''
