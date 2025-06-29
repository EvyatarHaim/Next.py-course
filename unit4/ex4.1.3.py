def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def first_prime_over(n):
    return next(number for number in range(n + 1, n * 100) if is_prime(number))
