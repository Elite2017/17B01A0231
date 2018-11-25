#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


def selfpowers(n):
    sum = 0
    i = 1
    while(i <= n):
      sum = sum + pow(i,i)
      i += 1
    return sum
print(selfpowers(1000))
     
