# Cindy Hernandez
# Mod 2.2
#10/27/24


def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2  # This part is correct

# Example usage
a = 5
b = 3  # Changed from "three" (string) to 3 (integer)
result = add_numbers(a, b)  # This will now work correctly
print("The sum of " + str(a) + " and " + str(b) + " is " + str(result) + ".")  # Now concatenates correctly
