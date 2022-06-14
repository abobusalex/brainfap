from sys import argv
import sys
import random

def interpretate(file):
    file = [x for x in file if x in ("-+,.><[]!1*^@20") ] # clear code text
    pointer = 0 # dataline pointer
    fileptr = 0 # file pointer
    stack = []  # stack
    dataline = [0] * 4096 # data line
    while (fileptr < len(file)):
        char = file[fileptr]
        # print(char)
        if (char == "+"): 
            dataline[pointer] += 1
        if (char == "-"):
            dataline[pointer] -= 1
        if (char == ">"):
            pointer += 1
        if (char == "<"):
            pointer -= 1
        if (char == "."):
            print(chr(dataline[pointer]), end="")
        if (char == ","):
            dataline[pointer] = ord(input()[0])

        if (char == "["):
            if (dataline[pointer] == 0):
                
                lb = 0
                while (True):
                    # How this works:
                    # it collects in lb (left bracket)
                    # quantity of [ when going forward
                    # to code. it decreases lb when
                    # ] has appeared. if [s and ]s 
                    # are even, it breaks the loop
                    fileptr += 1
                    char = file[fileptr]
                    # print(fileptr, char, lb)
                    if (char == "["): lb += 1
                    if (char == "]" and lb > 0 ):
                        lb -= 1
                        continue
                    if (char == "]" and lb == 0):
                        break

        if (char == "]"):
            if (dataline[pointer] != 0):
                rb = 0
                while (True):
                    fileptr -= 1
                    char = file[fileptr]
                    # print(fileptr, char, rb)
                    if (char == "]"): rb += 1
                    if (char == "[" and rb > 0 ):
                        rb -= 1
                        continue
                    if (char == "[" and rb == 0):
                        break
        # extended commands
        if (char == "!"):
            print(dataline[pointer], end="")
        if (char == "1"):
            print(dataline[pointer])
        if (char == "*"):
            stack.append(dataline[pointer])
        if (char == "^"):
            dataline[pointer] = stack.pop()
        if (char == "@"):
            dataline[pointer] = random.randint(0, 255)
        if (char == "2"):
            dataline[pointer] *= 2
        if (char == "0"):
            pointer = 0
            
        
        fileptr += 1



def main():
    if (len(argv) == 1):
        print("usage: {} file.bfap".format(argv[0]))
    else:
        file = open(argv[1],"r").read()
        interpretate(file)



main()