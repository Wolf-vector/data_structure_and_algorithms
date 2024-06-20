def two_indices(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

if __name__ == "__main__":
    sample_nums = [3,2,4]
    sample_target = 6
    result_indices = two_indices(sample_nums, sample_target)
    print(f"The indices of the two numbers that sum up to {sample_target} are: {result_indices}")