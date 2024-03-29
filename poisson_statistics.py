import numpy as np

def find_min_max_intervals(filename, num_intervals):
    # Read data from file
    with open(filename, 'r') as file:
        data = np.loadtxt(file)

    # Find minimum and maximum time moments
    min_time = np.min(data)
    max_time = np.max(data)

    # Calculate interval size
    interval_size = (max_time - min_time) / num_intervals

    # Break time into equal intervals
    intervals = np.linspace(min_time, max_time, num_intervals+1)

    # Compute counts for each interval
    counts = np.zeros(num_intervals, dtype=int)
    for i in range(num_intervals):
        counts[i] = np.sum((data >= intervals[i]) & (data < intervals[i+1]))

    return min_time, max_time, intervals, counts

# Function to read counts array from file
def read_counts_array(file_path):
    with open(file_path, 'r') as file:
        counts = np.loadtxt(file)
    return counts

# Function to save counts array to file
def save_counts_array(counts, file_path):
    np.savetxt(file_path, counts)

# File paths
file_paths = [r'C:\Users\patel\Code\T.1',
              r'C:\Users\patel\Code\T.2',
              r'C:\Users\patel\Code\T.3']

file_path = r'C:\Users\patel\Code\counts_array.txt'

# Read counts arrays from files
counts_arrays = [read_counts_array(file_path) for file_path in file_paths]

# Compute sample mean (m_bar) for each file
m_bar_array = np.mean(counts_arrays, axis=1)

# Compute sample mean of squared counts (m_squared_bar) for each file
m_squared_bar_array = np.mean(np.array(counts_arrays) ** 2, axis=1)

# Compute sample variance (squared deviation from the mean) for each file
sample_variance_array = m_squared_bar_array - m_bar_array**2

# Compute the parameter E for each data set
E_array = (sample_variance_array / m_bar_array) - 1

# Number of intervals
num_intervals = 100

# Print and save results
for i, file_path in enumerate(file_paths):
    print(f"File {i+1}: {file_path}")
    print("Sample Mean (m_bar):", m_bar_array[i])
    print("Sample Mean of Squared Counts (m_squared_bar):", m_squared_bar_array[i])
    print("Sample Variance (s^2):", sample_variance_array[i])
    print()

 # Save counts array to file
save_counts_array(counts_arrays[i], file_path)
print(f"Counts array saved to {file_path}")
print()

# Iterate through files
for i, file_path in enumerate(file_paths, start=1):
    min_time, max_time, intervals, counts = find_min_max_intervals(file_path, num_intervals)
    print(f"File {i}:")
    print(f"Minimum Time: {min_time}")
    print(f"Maximum Time: {max_time}")
    print(f"Number of Intervals: {num_intervals}")
    print("Intervals:")
    print(intervals)
    print("Counts:")
    print(counts)
    print()


