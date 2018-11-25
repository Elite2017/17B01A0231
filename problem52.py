#find the smallest positive integer x such that 2x,3x,4x,5x,6x contain the same digits?


def number(n):
    list = []
    while(n > 0):
      r = n % 10
      n = n / 10
      list.append(r)
    return list
for n in range(125874,1000000):
    list1 = number(n)
    list2 = number(2*n)
    list3 = number(3*n)
    list4 = number(4*n)
    list5 = number(5*n)
    list6 = number(6*n)
    print(set(list1) == set(list2))
    if((set(list1) == set(list2)) and (set(list2) == set(list3)) and (set(list3) == set(list4)) and (set(list4) == set(list5)) and (set(list5) == set(list6))):
       break
print(n)
