import csv


def remove_column(input_file, output_file, column_index):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Remove the column from each row
    modified_rows = [row[:column_index] + row[column_index + 1:]
                     for row in rows]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(modified_rows)

    print(
        f"Column {column_index} removed. Modified data saved to '{output_file}'.")


# Usage example
input_file = 'merged4.csv'  # Specify the path to your input CSV file
output_file = 'merged5.csv'  # Specify the path to the output CSV file
# Specify the index of the column you want to remove (0-based index)
column_index = 0

remove_column(input_file, output_file, column_index)
