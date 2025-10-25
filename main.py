def generate_euclid_numbers(n):
    """
    Generate the first n Euclid numbers.
    Euclid numbers are defined as E(n) = E(n-1) + 1 where E0 = 1
    and each number is the product of all previous numbers plus 1.
    """
    if n <= 0:
        return []
    
    euclid_numbers = [1]  # Initialize with E0 = 1
    
    for i in range(1, n):
        # Calculate product of all previous numbers
        product = 1
        for j in range(len(euclid_numbers)):
            product *= euclid_numbers[j]
        
        # Add 1 to get the next Euclid number
        next_number = product + 1
        euclid_numbers.append(next_number)
    
    return euclid_numbers

def main():
    # Generate first 5 Euclid numbers
    n = 5
    euclid_sequence = generate_euclid_numbers(n)
    
    print(f"First {n} Euclid numbers are:")
    for i, num in enumerate(euclid_sequence):
        print(f"E({i}) = {num}")

if __name__ == "__main__":
    main()
