def calculate_total_trek_length(A, B, C):
    total_distance =  (A + B + C) + (B - A) +(B - C)
    return total_distance

# Input values for A, B, and C
A = float(input("Enter the distance Amit beats Suman (in meters): "))
B = float(input("Enter the distance Amit beats Ravi (in meters): "))
C = float(input("Enter the distance Suman beats Ravi (in meters): "))

total_trek_length = calculate_total_trek_length(A, B, C)
print(f"The total length of the trek they all have traveled is: {total_trek_length} meters.")
