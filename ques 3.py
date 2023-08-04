def count_cat_dog(input_string):
    # Count occurrences of 'cat' and 'dog' in the input string
    cat_count = input_string.lower().count('cat')
    dog_count = input_string.lower().count('dog')
    
    # Return True if the counts are equal, otherwise False
    return cat_count == dog_count

# Get user input
user_input = input("Enter a string: ")

# Check if 'cat' and 'dog' appear the same number of times in the given string
result = count_cat_dog(user_input)

# Output the result

