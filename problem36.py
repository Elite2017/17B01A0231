def binary(n):
    s = ""
    while(n >= 2):
      r = n % 2
      n = n // 2
      s = s + str(r)
    s = s + str(n)
    s1 = s[::-1]
    return s1
def is_palindrome(n):
   # k = len(n)
    
    return(n == n[::-1])
sum = 0
for i in range(1,1000000):
    i1 = str(i)
    b = binary(i)
    b1 = b.lstrip("0")
    if(is_palindrome(b1) and is_palindrome(i1)):
      sum = sum + i
print(sum)
