def get_smallest_integer(my_list):
    if not my_list:
        raise ValueError("The list is empty.")
    return min(my_list)

if __name__ == "__main__":
    sample_list = [5, 3, 8, 2, 4]
    smallest_integer = get_smallest_integer(sample_list)
    print(f"The smallest integer in the list is: {smallest_integer}")