import csv


def remove_line_breaks(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Remove line breaks within each cell of the CSV
    clean_rows = [[cell.replace('\n', ' ').replace('\r', '')
                   for cell in row] for row in rows]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(clean_rows)

    print(f"Line breaks removed. Modified data saved to '{output_file}'.")


# Usage example
input_file = 'merged1.csv'  # Specify the path to your input CSV file
output_file = 'merged2.csv'  # Specify the path to the output CSV file

remove_line_breaks(input_file, output_file)
