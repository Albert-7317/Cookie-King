import os

def getCode(file):
    code = []
    codeFinal = []
    finalString = ''
    with open(file, 'r') as f:
        for line in f:
            code.append(line) 
    for line in code:
        start = line[2:] + '\r\n'
        codeFinal.append(start)
    for line in codeFinal:
        finalString = finalString + line 
    print(codeFinal)

getCode('test.txt')