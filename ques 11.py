def two_sum(nums, target):
    # Create an empty dictionary to store the numbers and their indices
    num_index_map = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement needed to achieve the target
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_index_map:
            # If it is, return the indices of the two numbers
            return [num_index_map[complement], i]
        else:
            # If it's not, add the current number and its index to the dictionary
            num_index_map[num] = i

    # If no solution is found, return an empty list or raise an exception
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
output = two_sum(nums, target)
print(output)  # Output: [0, 1]
