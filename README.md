# Poisson Statistics

This Python script is designed for the statistical analysis of multiple data sets. It includes functions to find minimum and maximum intervals, compute counts for each interval, read and save counts arrays, and calculate statistics such as sample mean, sample variance, and parameter E.

## Prerequisites

- Python 3.x
- NumPy

## Installation

No installation is required beyond having Python and NumPy installed.

## Set-up

1. Ensure your data files are in the appropriate format.
2. Adjust the `file_paths` variable to point to your data files.
3. Adjust the `file_path` variable to specify the path for saving the counts arrays.
4. Set the `num_intervals` variable to define the number of intervals for analysis.

## Functions

### `find_min_max_intervals(filename, num_intervals)`

- **Input**: 
  - `filename`: Path to the data file.
  - `num_intervals`: Number of intervals to divide the data into.
- **Output**: 
  - `min_time`: Minimum time moment in the data.
  - `max_time`: Maximum time moment in the data.
  - `intervals`: Array containing intervals.
  - `counts`: Array containing counts for each interval.

### `read_counts_array(file_path)`

- **Input**: 
  - `file_path`: Path to the file containing counts array.
- **Output**: 
  - `counts`: NumPy array containing counts.

### `save_counts_array(counts, file_path)`

- **Input**: 
  - `counts`: NumPy array containing counts to be saved.
  - `file_path`: Path to save the counts array.
