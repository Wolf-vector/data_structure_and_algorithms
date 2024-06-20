def find_first_occurrence(my_list, num):
    try:
        index = my_list.index(num)
        return index
    except ValueError:
        return -1  

if __name__ == "__main__":
    sample_list = [9, 6, 7, 2, 4, 3, 1]
    search_number = 7
    index = find_first_occurrence(sample_list, search_number)
    
    if index != -1:
        print(f"The first occurrence of {search_number} is at index: {index}")
    else:
        print(f"{search_number} is not found in the list.")