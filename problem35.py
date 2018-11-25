def is_prime(n):
    c = 0
    for i in range(2,n):
      if(n % i == 0):
        c = c + 1
    return(c == 0)

count = 0
n = int(input())
for num in range(2,n):
    num = str(num)
    q = False
    for i in range(len(num)):
        if(is_prime(int(num[i:] + num[:i]))):
          q = True
        else:
          q = False
          break    
    if q:
        count = count + 1
print(count)
