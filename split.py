import os
import sys

def main():
    currentDir = os.path.dirname(os.path.realpath(__file__))
    args = sys.argv
    print(args)
    f = open(args[1])
    
    line = f.readline()
    while line:
        strs = line.split()
   
        if strs[1] == "Begin":
            fileName = strs[4] + "_split.txt"
            output = open(fileName, 'w')
        output.write(line)
        if strs[1] == "End":
           output.close
        line = f.readline()
    f.close
    print("Done")

if __name__ == "__main__":
    main()
