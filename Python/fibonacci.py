def fibonacci(n):
    # Initialize the first two terms of the sequence
    fib_sequence = [0, 1]
    # Check if n is less than or equal to 0
    if n <= 0:
        return []
    # Check if n is 1, return the first term
    elif n == 1:
        return [0]
    # Generate the Fibonacci sequence up to the nth term
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence

# Example: Print the first 10 Fibonacci numbers
n = 10
fib_series = fibonacci(n)
print(fib_series)