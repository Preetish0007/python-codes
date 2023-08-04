def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_gcd_of_list(numbers_list):
    if len(numbers_list) < 2:
        return None  # The list should have at least 2 elements to find the GCD

    result = numbers_list[0]
    for i in range(1, len(numbers_list)):
        result = gcd(result, numbers_list[i])

    return result

# Taking user input for the list of numbers
user_input = input("Enter a list of two or more numeric values separated by spaces: ")
numbers_list = list(map(int, user_input.split()))

# Finding the GCD of the numbers in the list
gcd_result = find_gcd_of_list(numbers_list)

if gcd_result is not None:
    print(f"The GCD of the numbers in the list is: {gcd_result}")
else:
    print("Please enter a valid list with at least 2 numeric values.")
