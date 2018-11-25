#What is the sum of the digits of the number 21000?

sum = 0
def powdigitsum(n):
  global sum
  while(n != 0):
    r = n % 10
    sum = sum + r
    n = n / 10
  return sum
num = pow(2,1000)
print(powdigitsum(num))

    
