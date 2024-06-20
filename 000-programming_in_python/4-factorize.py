def factorize(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    sample_number = 52
    prime_factors = factorize(sample_number)
    print(f"The prime factors of {sample_number} are: {prime_factors}")