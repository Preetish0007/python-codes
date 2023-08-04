def convert_paragraph_to_list(input_str):
    # Split the input paragraph into individual words
    words = input_str.split()

    # Initialize an empty list to store words with more than 4 letters
    long_words_list = []

    # Iterate through each word and check if it has more than 4 letters
    for word in words:
        # Remove punctuation marks from the word, if any
        clean_word = word.strip()

        if len(clean_word) > 4:
            long_words_list.append(clean_word)

    return long_words_list

def main():
    # Take input from the user
    input_paragraph = input("Enter a paragraph or sentence: ")

    # Convert the input paragraph to a list of words with more than 4 letters
    result_list = convert_paragraph_to_list(input_paragraph)

    # Print the result
    print("List of words with more than 4 letters:")
    print(result_list)

if __name__ == "__main__":
    main()
