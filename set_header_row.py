import pandas as pd


def set_header_row(input_file, output_file):
    # Read the CSV file into a DataFrame, specifying the first row as the header
    df = pd.read_csv(input_file, header=0)

    # Write the DataFrame to a new CSV file with the header row
    df.to_csv(output_file, index=False)

    print(f"Header row set. Modified data saved to '{output_file}'.")


# Usage example
input_file = 'tw.csv'  # Specify the path to your input CSV file
output_file = 'twh.csv'  # Specify the path to the output CSV file

set_header_row(input_file, output_file)
