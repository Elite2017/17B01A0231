#find the sum of all the numbers which are equal to the sum of the factorial of their digits?


def num_digits(n):
    n1 = n
    sum = 0
    list = []
    while(n > 0):
       r = n % 10
       n = n / 10
       i = fact(r)
       sum = sum + i
    return (sum == n1)
def fact(x):
    factorial = 1
    while(x != 1):
      factorial = factorial * x
      x = x - 1
    return factorial
def sumtotal():
    sum = 0
    for i in range(145,100000):
      if(num_digits(i)):
        sum = sum + i
    return sum
      
print(sumtotal())
    
