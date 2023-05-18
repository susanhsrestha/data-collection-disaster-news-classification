import csv
import re


def normalize_spaces(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Normalize spaces in each field of the CSV
    clean_rows = [[re.sub(r'\s+', ' ', field.strip())
                   for field in row] for row in rows]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(clean_rows)

    print(f"Spaces normalized. Modified data saved to '{output_file}'.")


# Usage example
input_file = 'merged3.csv'  # Specify the path to your input CSV file
output_file = 'merged4.csv'  # Specify the path to the output CSV file

normalize_spaces(input_file, output_file)
