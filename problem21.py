#Evaluate the sum of all amicable numbers under 10000

l = []
def amicablenum():
    global l
    for i in range(10000):
      if(i not in l):
       sumofdivisor =  divisor(i)
      if(divisor(sumofdivisor) == i and (sumofdivisor != i)):
       l.append(i)
       l.append(sumofdivisor)
    return l

def divisor(n):
  sumofdiv = 0
  for j in range(1,n):
    if(n % j == 0):
      sumofdiv = sumofdiv + j
  return sumofdiv

sumofamic = 0
listofamic = []
listofamic = amicablenum()
for i in listofamic:
    sumofamic = sumofamic + i
print(sumofamic)
