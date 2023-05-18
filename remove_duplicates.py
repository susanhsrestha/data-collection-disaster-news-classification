import pandas as pd


def remove_duplicate_rows(input_file, output_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Write the modified DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Duplicate rows removed. Modified data saved to '{output_file}'.")


# Usage example
input_file = 'merged5.csv'  # Specify the path to your input CSV file
output_file = 'merged6.csv'  # Specify the path to the output CSV file

remove_duplicate_rows(input_file, output_file)
