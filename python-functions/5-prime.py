def is_prime(n):
    for i in range(2,n):
        if (n%i):
            return False
        return True
print(is_prime(3))
print(is_prime(8))
print(is_prime(9))
print(is_prime(13))




