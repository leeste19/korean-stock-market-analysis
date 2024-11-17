import os
import pandas as pd

# Define the directory containing the files
directory = "~/korean-stock-market-analysis/data"
directory = os.path.expanduser(directory)

# Initialize variables
total_rows_original = 0
merged_rows = 0

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the pattern
    if filename.startswith("KOSPI_200_2") and filename.endswith(".csv"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file to count rows
        df = pd.read_csv(file_path)
        num_rows = len(df)
        total_rows_original += num_rows
        print(f"File: {filename}, Rows: {num_rows}")

# Load the merged file
merged_file = os.path.join(directory, "KOSPI_200_merged.csv")
merged_df = pd.read_csv(merged_file)
merged_rows = len(merged_df)

print(f"\nTotal rows in original files: {total_rows_original}")
print(f"Total rows in merged file: {merged_rows}")

# Compare row counts
if total_rows_original == merged_rows:
    print("✅ Verification successful: All rows are included in the merged file.")
else:
    print("❌ Verification failed: Mismatch in row counts.")

