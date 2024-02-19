import pandas as pd
import os

# Specify the folder containing the Excel files
folder_path = r'C:\Users\Christoph\Documents\Master Thesis\Energy Consumption'
output_folder_path = r'C:\Users\Christoph\Documents\Master Thesis\Energy Consumption\Finished_Files'

# List all Excel files in the folder (excluding temporary files)
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') and not f.startswith('~$')]

print("Excel files found with indices:")
for i, file in enumerate(excel_files):
    print(f"{i}: {file}")

# Example: Select files by indices
print("Please enter the indices of up to three Excel files to merge, separated by commas (e.g., 0,1,2):")
selected_indices_input = input()  # Example input: 0,1,2

# Convert the input string to a list of integers
selected_indices = [int(index.strip()) for index in selected_indices_input.split(',') if index.strip().isdigit()]

# Ensure the selected indices are within the range of available files
selected_indices = [index for index in selected_indices if index < len(excel_files)]

# Select files based on the chosen indices
selected_files = [excel_files[index] for index in selected_indices]
print(f"\nSelected files: {selected_files}")

# Initialize an empty DataFrame to store merged data
dfs = []

# Loop through the selected files, read each into a DataFrame
for file in selected_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path, usecols="A:D")  # Adjust 'usecols' as needed
    dfs.append(df)

# Concatenate the DataFrames side by side
merged_df = pd.concat(dfs, axis=1)


output_name = selected_files[0].split("_")
name = output_name[0:7]
name_xlsx = "Merged_" + "_".join(name) +".xlsx"

# Define the path for the merged Excel file within the output folder
output_file_path = os.path.join(output_folder_path, name_xlsx)

# Save the merged DataFrame to the new Excel file
merged_df.to_excel(output_file_path, index=False)

print(f'\nMerged file saved to {output_file_path}')
