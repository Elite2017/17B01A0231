#what is the value of the first triangular number to have over five hundred divisors?


def triangularnum():
  trnum = 0
  i = 1
  while(divisor(trnum) < 500):
    trnum = trnum + i
    i += 1
  return trnum
def divisor(n):
  c = 0
  for j in range(1,n + 1):
    if(n % j == 0):
      c = c + 1
  return c
print(triangularnum())
  
