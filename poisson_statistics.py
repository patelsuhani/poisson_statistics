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

    return min_time, max_time, intervals

# File paths
file_paths = [r'C:\Users\patel\Code\T.1',
              r'C:\Users\patel\Code\T.2',
              r'C:\Users\patel\Code\T.3']

# Number of intervals
num_intervals = 100

# Iterate through files
for i, file_path in enumerate(file_paths, start=1):
    min_time, max_time, intervals = find_min_max_intervals(file_path, num_intervals)




