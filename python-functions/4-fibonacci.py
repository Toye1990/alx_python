def fibonacci_sequence(n):   
        a, b = 0, 1
while a < n:
 print(a, end=' ')
 a, b = b, a+b
 print()

# Now call the function we just defined:
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
