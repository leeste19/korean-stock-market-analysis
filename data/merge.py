import os
import pandas as pd

# Define the directory containing the files
directory = "~/korean-stock-market-analysis/data"
directory = os.path.expanduser(directory)

# Initialize an empty list to store DataFrames
dataframes = []

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the pattern
    if filename.startswith("KOSPI_200_") and filename.endswith(".csv"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        print(file_path)        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Append the DataFrame to the list
        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged DataFrame to a new CSV file
output_file = os.path.join(directory, "KOSPI_200_merged.csv")
merged_df.to_csv(output_file, index=False)

print(f"All files merged successfully into '{output_file}'")

