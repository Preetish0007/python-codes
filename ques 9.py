def factorial(n):
    """
    Calculate the factorial of a number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def permutations(n, r):
    """
    Calculate the number of permutations of n objects taken r at a time.
    """
    if n < r:
        return "Error: n must be greater than or equal to r"
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    """
    Calculate the number of combinations of n objects taken r at a time.
    """
    if n < r:
        return "Error: n must be greater than or equal to r"
    return permutations(n, r) // factorial(r)

# Example usage:
n = 5
r = 3

print("Permutations of {} objects taken {} at a time: {}".format(n, r, permutations(n, r)))
print("Combinations of {} objects taken {} at a time: {}".format(n, r, combinations(n, r)))
