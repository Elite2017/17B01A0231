#combinatoric selections

def ncr(n,r):
    m = fact(n)/((fact(r))*(fact(n - r)))
    return m
def fact(x):
    factorial = 1
    while(x != 1):
      factorial = factorial * x
      x = x - 1
    return factorial
count = 0
for i in range(1,101):
    for j in range(1,i):
        k = ncr(i,j)
        if(k > 1000000):
          count = count + 1
print(count)
    
