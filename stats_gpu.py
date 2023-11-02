import os
import json
import pandas as pd
import datetime

# Directory containing the JSON files
json_directory = r'C:\Users\Christoph\Documents\CapFrameX\Captures'

# List all JSON files in the directory
json_files = [file for file in os.listdir(json_directory) if file.endswith('.json')]

# Display the list of available JSON files
print("Available JSON files:")
for i, file in enumerate(json_files):
    print(f"{i + 1}: {file}")

# Prompt so that I can select the file I want to analyze
while True:
    try:
        selected_index = int(input("Enter the index of the JSON file to analyze: ")) - 1
        if 0 <= selected_index < len(json_files):
            selected_file = json_files[selected_index]
            break
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Construct the full file path for the selected JSON file
json_file_path = os.path.join(json_directory, selected_file)

# Extract the game name from the selected JSON file's name and remove ".exe"
game_name = selected_file.split('-')[1].replace('.exe', '')  # Assumes a consistent naming format

# Open and read the selected JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    print(data.keys())
    x = data["Runs"][0]
    y = x["CaptureData"]
    frame_times = y["MsBetweenPresents"]
    print(frame_times)

df = pd.DataFrame(frame_times)
df = df.rename(columns={0: "FrameTime"})
print(df)

now = datetime.datetime.now()
timestamp = now.strftime("%m_%d_%H_%M")  # Example: "10_30_11_44"

# Define the target directory and include the game name in the output_file_name
output_directory = r"C:\Users\Christoph\Documents\Master Thesis\Frametimes"
output_file_name = f"benchmark_{game_name}_{timestamp}.xlsx"

# Full file path for the output
output_file_path = os.path.join(output_directory, output_file_name)

# Save the DataFrame to Excel
df.to_excel(output_file_path, index=True)

print(f"DataFrame saved to {output_file_path}")
