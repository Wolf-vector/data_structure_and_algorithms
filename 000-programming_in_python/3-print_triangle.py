def print_right_triangle(height):
    for i in range(1, height + 1):
        print("*" * i)

if __name__ == "__main__":
    sample_height = 8
    print("Right-angled triangle:")
    print_right_triangle(sample_height)