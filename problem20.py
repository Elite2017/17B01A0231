#to find factorial of a number


fact = lambda x : 1 if x == 0 else x * fact(x - 1)
x = int(input())
factorial = fact(x)

#to find sum of digits of the factorial
sum_digits = lambda number: 0 if number == 0 else (number % 10) + sum_digits (number / 10)
print(sum_digits(factorial))

