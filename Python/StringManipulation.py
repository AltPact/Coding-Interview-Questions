def count_characters(input_str):
    return len(input_str)

def find_substrings(input_str, substring):
    return input_str.count(substring)

def reverse_words(input_str):
    words = input_str.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


print(count_characters("Hello, World!"))  # Output: 13
print(find_substrings("Hello, World! Hello, Python!", "Hello"))  # Output: 2
print(reverse_words("Hello, World!"))  # Output: "olleH, dlroW!"