import os

# Define the mapping between (n) and years
mapping = {
    1: 2023, 2: 2022, 3: 2021, 5: 2020, 6: 2019,
    7: 2018, 8: 2017, 10: 2016, 11: 2015, 12: 2014,
    13: 2013, 14: 2012, 15: 2011, 16: 2010, 17: 2009, 18: 2008
}

# Directory containing the files
directory = "~/korean-stock-market-analysis/data"

# Expand user directory
directory = os.path.expanduser(directory)

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the filename starts with "Download"
    if filename.startswith("Download Data - INDEX_XX_KOREA EXCHANGE"):
        # Extract the number in parentheses
        start_idx = filename.find('(')
        end_idx = filename.find(')')
        
        if start_idx != -1 and end_idx != -1:
            # Extract the number and convert it to an integer
            number = int(filename[start_idx + 1:end_idx])
            
            # Check if the number is in the mapping
            if number in mapping:
                # Construct the new filename
                new_filename = f"KOSPI_200_{mapping[number]}.csv"
                
                # Rename the file
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")

