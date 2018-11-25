#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

sumfp = 0
def fourthpowers(n):
  sum = 0
  n1 = n
  while(n != 0):
   digit = n % 10
   n = n / 10
   sum = sum + pow(digit,5)
  if(sum == n1):
    print(n1)
  return(n1 == sum)
def sumoffourthpow():
 global sumfp
 for n in range(10,355000):
   sum =  fourthpowers(n)
   if(sum):
     sumfp = sumfp + n
 return sumfp
print("sum is",sumoffourthpow())
  
