from sys import argv
import sys

def interpretate(file):
    file = [x for x in file if x in ("-+,.><[]") ]
    pointer = 0
    fileptr = 0
    dataline = [0] * 4096
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
                
        fileptr += 1



def main():
    if (len(argv) == 1):
        print("usage: {} file.bfap".format(argv[0]))
    else:
        file = open(argv[1],"r").read()
        interpretate(file)



main()