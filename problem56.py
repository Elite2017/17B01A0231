#considering natural numbers of the form a^b, where a,b < 100 what is the maximum digital sum?


def power_sum(a,b):
    sum = 0
    n = pow(a,b)
    while(n > 0):
      r = n % 10
      n = n / 10
      sum = sum + r
    return sum
max = 0
for i in range(1,100):
    for j in range(1,100):
     sum = power_sum(i,j)
     if(sum > max):
       max = sum
print(max)
    
