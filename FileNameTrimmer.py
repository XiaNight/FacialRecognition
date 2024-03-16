# Read CSV in a target file to data

import os
import csv
print("Reading CSV file")

target_file = "full_path_data.csv"

# data saved with 1 row seperated with comma

data = None

with open(target_file, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

print(data[0])
