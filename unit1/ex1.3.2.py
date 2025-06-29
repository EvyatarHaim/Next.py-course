def is_prime(number):
    return number > 1 and not [True for num in range(2, number) if number % num == 0]
