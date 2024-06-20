def character_frequency(string):
    frequency_dict = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict

if __name__ == "__main__":
    sample_string = "Hello, World! This is a test string."
    result = character_frequency(sample_string)
    print("Character frequency:")
    for char, freq in result.items():
        print(f"{char}: {freq}")