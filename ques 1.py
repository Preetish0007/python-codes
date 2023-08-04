def merge_lists_into_dictionary(keys, values):
    return dict(zip(keys, values))

def main():
    try:
        size = int(input("Enter the size of the lists: "))
        if size <= 0:
            raise ValueError("Size must be a positive integer.")

        print("Enter elements for the first list:")
        list1 = []
        for i in range(size):
            element = input(f"Enter element {i+1}: ")
            list1.append(element)

        print("\nEnter elements for the second list:")
        list2 = []
        for i in range(size):
            element = input(f"Enter element {i+1}: ")
            list2.append(element)

        dictionary_name = input("\nEnter the name of the dictionary: ")

        merged_dict = merge_lists_into_dictionary(list1, list2)

        print(f"\nMerged dictionary '{dictionary_name}':")
        print(merged_dict)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
