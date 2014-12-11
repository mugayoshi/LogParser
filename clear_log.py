from __future__ import print_function
import glob
import os

import re
import string
def filter(line, argID):
  
    if line.find('Modify'):
        arry = line.split(':')
        hasID = 0
        method_top = 0
        log = ''
        ID = 0
        string = []
        for x in arry:
            
            if x.find('ID') != -1:
                hasID = 1

            elif x.find('CLASS') != -1:
                method_top = 1;
                              
            if (hasID == 1 or method_top == 1):
                log += x
                
        if (hasID == 1):
            ID = log[1]
    
        string = log.split(" ")

        if len(log) > 1:
    
            print(log.strip())
            return ID
    else:
        return '0'
    

 


def main():
    current = os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(current):
        if (file.endswith(".txt") and 'imatch' in file):
            print("Do you wanna see " + file + "?")
            input_ans = raw_input()
            if (input_ans.find('y') != -1 or input_ans.find('Y') != -1):
                break
            
    f = open(file)
    line = f.readline()
    ID = 0
    while line:
        ID = filter(line, ID)
        line = f.readline()
    f.close

if __name__ == "__main__":
    main()
