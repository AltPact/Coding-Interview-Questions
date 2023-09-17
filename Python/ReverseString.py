def reverse_string(input_str):
    return input_str[::-1]

if __name__ == "__main__":
    input_str = "Hello, World!"
    reversed_str = reverse_string(input_str)
    print("Reversed:", reversed_str)