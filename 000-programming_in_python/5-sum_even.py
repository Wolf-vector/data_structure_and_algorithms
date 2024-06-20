def sum_even_numbers(my_list):
    return sum(num for num in my_list if num % 2 == 0)

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sum_even_numbers(sample_list)
    print(f"The sum of even numbers in the list is: {result}")