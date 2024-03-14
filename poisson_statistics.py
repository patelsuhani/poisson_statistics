import numpy as np

def find_min_max_intervals(filename, num_intervals):
    # Read data from file
    with open(filename, 'r') as file:
        data = np.loadtxt(file)

    # Find minimum and maximum time moments
    min_time = np.min(data)
    max_time = np.max(data)
