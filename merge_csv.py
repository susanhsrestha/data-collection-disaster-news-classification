import pandas as pd
import glob


def merge_csv_files(input_folder, output_file):
    # Get a list of all CSV files in the input folder
    file_paths = glob.glob(input_folder + '/*.csv')

    # Initialize an empty list to store dataframes
    dfs = []

    # Iterate over the CSV files
    for file_path in file_paths:
        # Read each CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Append the DataFrame to the list
        dfs.append(df)

    # Concatenate the list of dataframes into a single dataframe
    merged_df = pd.concat(dfs, ignore_index=True)

    # Write the merged DataFrame to a new CSV file
    merged_df.to_csv(output_file, index=False)

    print(f"CSV files merged. Merged data saved to '{output_file}'.")


# Usage example
# Specify the path to the folder containing the input CSV files
input_folder = 'input_folder'
output_file = 'merged.csv'  # Specify the path to the output CSV file

merge_csv_files(input_folder, output_file)
