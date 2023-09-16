def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]

# Example usage:
input_str = "Was It A Rat I Saw?"
result = is_palindrome(input_str)
print(result)  # Output: True