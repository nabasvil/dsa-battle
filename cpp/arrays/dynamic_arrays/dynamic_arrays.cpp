#include <iostream>
#include <vector>
#include <chrono>

void measure_vector_performance(long long num_elements) {
    std::cout << "--- Measuring C++ std::vector append performance ---" << std::endl;

    // Allocate memory upfront for better performance (optional)
    std::vector<int> my_vector;
    my_vector.reserve(num_elements);

    auto start = std::chrono::high_resolution_clock::now();

    for (long long i = 0; i < num_elements; ++i) {
        my_vector.push_back(i);
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    std::cout << "Time to append " << num_elements << " elements: " << duration.count() << " seconds" << std::endl;
}

int main() {
    long long data_sizes[] = { 100000, 1000000, 10000000 };

    for (long long size : data_sizes) {
        measure_vector_performance(size);
    }

    return 0;
}