import csv
import re


def remove_links(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Remove links from each field in the CSV
    clean_rows = [[re.sub(r"http\S+|www\S+", "", field)
                   for field in row] for row in rows]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(clean_rows)

    print(f"Links removed. Modified data saved to '{output_file}'.")


# Usage example
input_file = 'merged2.csv'  # Specify the path to your input CSV file
output_file = 'merged3.csv'  # Specify the path to the output CSV file

remove_links(input_file, output_file)
