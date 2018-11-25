#find the pair of pentagonal numbers for which their sum and difference is pentagonal find the difference of that pair of numbers?

def pent():
  ps = set()
  i = 1000
  while True:
    i += 1
    s = (3 * i* i - i)//2
    for pj in ps:
      if s - pj in ps and s - 2*pj in ps:
         return s - 2*pj
    ps.add(s) 
    
print(pent())
    
