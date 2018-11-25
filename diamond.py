#program to print diamond pattern

STAR = "*"
CRLF = "\n"
SPACE = " "
rows = 7
SIZE = (rows*2)-1

SP = STAR
RP = STAR + STAR
EP = CRLF


def diamond():
    diamond = ""
    for line in range(SIZE):
        if(line < rows):
            diamond += aLine(line)
        else:
            diamond += raLine(line)
    return diamond
def aLine(line):
    return leadingSpace(line) + StartPattern(line) + repeatPattern(line) + endPattern(line)

def leadingSpace(n):
    return ((rows - n)-1)*SPACE

def StartPattern(n):
    return STAR

def repeatPattern(n):
    return n * RP

def endPattern(n):
    return EP


def revleadingSpace(n):
    return ((n - rows) + 1)*SPACE

def revrepeatPattern(n):
    return ((SIZE - n) - 1)*RP

def raLine(line):
    return revleadingSpace(line) + StartPattern(line) + revrepeatPattern(line) + endPattern(line)


print(diamond())
    
