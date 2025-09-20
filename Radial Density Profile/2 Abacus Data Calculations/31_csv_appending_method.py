import csv

# Define your data to be written to the CSV
data = [
    ['Column1', 'Column2', 'Column3'],  # Header row
    # Example data rows
    [1, 'A', 10.5],
    [2, 'B', 20.3],
    [3, 'C', 15.8]
]

# Specify the filename for the CSV file
filename = 'data.csv'

# Open the CSV file in append mode
with open(filename, 'a', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Loop through your data and append each row to the CSV file
    for row in data:
        csvwriter.writerow(row)

print("Data appended to", filename)
