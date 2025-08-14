import timeit


def measure_append_performance(num_elements):
    """Measures the time it takes to append elements to a Python list."""
    setup_code = "my_list = []"
    test_code = f"for i in range({num_elements}): my_list.append(i)"
    
    # Run the test 10 times and get the average duration
    duration = timeit.timeit(test_code, setup=setup_code, number=10) 
    print(f"Time to append {num_elements} elements: {duration:.6f} seconds")
    return duration


if __name__ == "__main__":
    # Test on different data sizes
    data_sizes = [100_000, 1_000_000, 10_000_000]
    results = {}
    
    print("--- Measuring Append Performance ---")
    for size in data_sizes:
        time_taken = measure_append_performance(size)
        results[f'append_{size}'] = time_taken

    # The results can be saved for later visualization, e.g., in a CSV file.
    # For now, let's just print them
    print("\nFinal Results:")
    for key, value in results.items():
        print(f"{key}: {value:.6f}s")