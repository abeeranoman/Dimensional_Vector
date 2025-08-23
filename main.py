def main():
    # Creating vectors for demonstration
    vec_a = Vector([2, 4, 6])
    vec_b = Vector([1, 3, 5])
    
    # Show original vectors
    print("Vector A:", vec_a)
    print("Vector B:", vec_b)
    
    # Addition of two vectors
    sum_vec = vec_a + vec_b
    print("A + B =", sum_vec)
    
    # Subtracting vectors
    diff_vec = vec_a - vec_b
    print("A - B =", diff_vec)
    
    # Check equality and inequality
    print("A == B?", vec_a == vec_b)
    print("A != B?", vec_a != vec_b)
    
    # Accessing and changing vector elements
    vec_a[0] = 10
    print("Modified Vector A:", vec_a)
    print("First element of modified A:", vec_a[0])
    
    # Example of mismatched addition (should trigger exception)
    short_vec = Vector([1, 2])
    try:
        result = vec_a + short_vec
    except ValueError as err:
        print("Caught an error while adding vectors of different lengths:", err)

# Execute the tests only if this script is run directly
if __name__ == "__main__":
    main()