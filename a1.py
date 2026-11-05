def generate_fibonacci(terms):
    """
    Generates a list containing the Fibonacci sequence up to the specified number of terms.
    """
    if terms <= 0:
        return []
    elif terms == 1:
        return [0]
    
    # Initialize the first two terms of the sequence
    sequence = [0, 1]
    
    # Calculate subsequent terms up to the requested count
    for _ in range(2, terms):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence

# Example usage:
if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
        result = generate_fibonacci(num_terms)
        print(f"Fibonacci sequence ({num_terms} terms): {result}")
    except ValueError:
        print("Please enter a valid integer.")
