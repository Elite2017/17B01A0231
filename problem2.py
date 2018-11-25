
a = 1
b = 2
pa = 0
sumofpa = 2
for i in range(0,10000):
  pa = a + b
  a = b
  b = pa
  if(pa % 2 == 0 and pa < 4000000):
    sumofpa = sumofpa + pa
print(sumofpa)   
