from __future__ import print_function
import glob
import os

import re
import string
   
def  makeSentence(line):
    if line.find('Modify'):
        if (line.find('ID') == -1 and line.find('CLASS') == -1):
            return ''
        arry = line.split(':')
        hasID = 0
        method_top = 0
        log = ''
        string = []
        for x in arry:
            
            if x.find('ID') != -1:
                hasID = 1

            elif x.find('CLASS') != -1:
                method_top = 1;
                              
            if (hasID == 1 or method_top == 1):
                log += x
                
        return log
    else:
        return ''
 
def getIDAndTag(line):
    log = []
    log = line.split()
    i = 0
    for x in log:
        if x == "ID":
            break
        if x == "CLASS":
            return (0,"CLASS")
        i += 1
    print(i)
    ID = log[i + 1]
    tag = log[i + 2]
    
    return (ID, tag)

def checkID(arry, ID):
    if len(arry) < 1:
        return 0
    for i in arry:
        if i == ID:
            return 1
    return 0

def findClass(line):
    log = []
    log = line.split()
#    print(log)
    i = 0
    for x in log:
        if x == "In":
            break
        if x == "CLASS":
            break
        i += 1
  #  print(i)
    className = log[i + 1]
    package = re.split('[ .]', className)
    lenPackage = len(package)
    
    return package[lenPackage - 1]
            
 
def addOutputFile(file, outputs):
    for x in outputs:
        if x == file:
            return 0
    return 1

def refine(file):
    f = open(file)
    line = f.readline()
    IDs = []

    outputFile = "refined_" + file
    output = open(outputFile, 'w')
    while line:
        tab_str = ''
        log = makeSentence(line)
        if len(log) > 1:

            ID, tag = getIDAndTag(log)
            if tag == 'Before':
                IDs.append(ID)
            for i in range(len(IDs)):
                tab_str += '\t'
            output.write(tab_str +  log)

            if tag == 'After':
                if checkID(IDs, ID) == 1:
                    IDs.remove(ID)

        line = f.readline()

    f.close
    
def main():
    current = os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(current):
        if (file.endswith(".txt") and 'imatch' in file):
            print("Do you wanna see " + file + "?")
            input_ans = raw_input()
            if (input_ans.find('y') != -1 or input_ans.find('Y') != -1):
                break
            
    f = open(file)
    print("Writing Start!")
    line = f.readline()
#    IDs = []
    lineNum = 0
    outputs = []
    while line:
        tab_str = ''
        log = makeSentence(line)
        if len(log) > 1:
            className = findClass(log)
            outputFile = className + "_splited_" + file
            if addOutputFile(outputFile, outputs) == 1:
                outputs.append(outputFile)
            output = open(outputFile, 'a+')
            output.write(str(lineNum) + ":" +  log)
            lineNum += 1
        line = f.readline()

    f.close

    for x in outputs:
        refine(x)
        os.remove(x)

    print("Writing Done!")

if __name__ == "__main__":
    main()
