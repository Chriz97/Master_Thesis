import os
import json
import pandas as pd
import datetime

# Define the directory containing the JSON files
json_directory = r'C:\Users\Christoph\Documents\CapFrameX\Captures'

# List all JSON files in the directory
json_files = [file for file in os.listdir(json_directory) if file.endswith('.json')]

# Display the list of available JSON files
print("Available JSON files:")
for i, file in enumerate(json_files):
    print(f"{i + 1}: {file}")

# Prompt the user to select a file by index
while True:
    try:
        selected_index = int(input("Enter the index of the JSON file you want to analyze: ")) - 1
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
game_name = selected_file.split('-')[1].replace('.exe', '')
if game_name == "cod":
    game_name = "Modern Warfare III"

# Open and read the selected JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    x = data["Runs"][0]
    y = x["CaptureData"]
    frame_times = y["MsBetweenPresents"]

df = pd.DataFrame(frame_times)
df = df.rename(columns={0: "FrameTime"})

now = datetime.datetime.now()
timestamp = now.strftime("%m_%d_%H_%M")  # Example: "10_30_11_44"

technologies = ["DLSS", "XeSS", "FSR"]
upscaling_setting = ["Performance", "Balanced", "Quality"]
graphics_settings = ["Low", "Medium", "High"]
resolution = ["1080p", "1440p"]

# Prompt user to select options by index
tech_index = int(input(f"Select the technology ({', '.join([f'{i}: {tech}' for i, tech in enumerate(technologies)])}): "))
upscaling_index = int(input(f"Select the upscaling setting ({', '.join([f'{i}: {setting}' for i, setting in enumerate(upscaling_setting)])}): "))
graphics_index = int(input(f"Select the graphics setting ({', '.join([f'{i}: {setting}' for i, setting in enumerate(graphics_settings)])}): "))
resolution_index = int(input(f"Select the resolution ({', '.join([f'{i}: {res}' for i, res in enumerate(resolution)])}): "))

# Validate selections
if tech_index not in range(len(technologies)) or \
   upscaling_index not in range(len(upscaling_setting)) or \
   graphics_index not in range(len(graphics_settings)) or \
   resolution_index not in range(len(resolution)):
    print("One or more invalid selections. Please restart and enter valid index numbers.")


# Define the target directory and include the game name in the output_file_name
output_directory = r"C:\Users\Christoph\Documents\Master Thesis\Frametimes"
output_file_name = f"benchmark_{game_name}_{technologies[tech_index]}_{upscaling_setting[upscaling_index]}_{graphics_settings[graphics_index]}_{resolution[resolution_index]}_{timestamp}.xlsx"

# Full file path for the output
output_file_path = os.path.join(output_directory, output_file_name)

# Save the DataFrame to Excel
df.to_excel(output_file_path, index=True)

print(f"DataFrame saved to {output_file_path}")


