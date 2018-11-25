def pandigital(n):
  list = []
  for i in range(1,n):
    for j in range(1,n):
      a = i * j
      s = str(a)+str(i)+str(j)
      if(len(s) == 9):
        s1 = sorted(s)
        c = 0
        for k in range(len(s1)):
            if(s1[k] != str(k + 1)):
              c = c + 1
        if(c == 0):
              list.append(a)
  return(sum(set(list)))
print(pandigital(10000))
