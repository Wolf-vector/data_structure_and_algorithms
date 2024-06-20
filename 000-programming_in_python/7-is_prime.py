def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True

if __name__ == "__main__":
    sample_number = 2548
    if is_prime(sample_number):
        print(f"{sample_number} is a prime number.")
    else:
        print(f"{sample_number} is not a prime number.")