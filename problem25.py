#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def thousandfib(a,b):
    result = 2
    while(len(str(b)) < 1000):
     a , b = b , a + b
     result = result + 1
    return result
print(thousandfib(1,1))
