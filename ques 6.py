def even_filter(input_list):
    return [num for num in input_list if num % 2 == 0]

def odd_filter(input_dict):
    return {key: value for key, value in input_dict.items() if value % 2 != 0}

# Example usage
if __name__ == "__main__":
    # User-defined list of numbers
    user_list_str = input("Enter a list of numbers separated by spaces: ")
    user_list = [int(num) for num in user_list_str.split()]

    # User-defined dictionary with number as key and value
    user_dict = {}
    while True:
        key = input("Enter a key (or 'exit' to stop): ")
        if key.lower() == 'exit':
            break
        value = int(input("Enter the corresponding value: "))
        user_dict[key] = value

    # Calling the even_filter function with the list as an argument
    even_numbers = even_filter(user_list)
    print("Even numbers:", even_numbers)

    # Calling the odd_filter function with the dictionary as an argument
    odd_numbers_dict = odd_filter(user_dict)
    print("Odd numbers from the dictionary:")
    for key, value in odd_numbers_dict.items():
        print(f"{key}: {value}")
