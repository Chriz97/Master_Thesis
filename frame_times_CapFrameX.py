import os
import json
import pandas as pd
import datetime

# Define the directory containing the JSON files
json_directory = r'C:\Users\Christoph\Documents\CapFrameX\Captures'

# List all JSON files in the directory
json_files = [file for file in os.listdir(json_directory) if file.endswith('.json')]

# Display the list of available JSON files along with their creation times
print("Available JSON files:")
for i, file in enumerate(json_files):
    file_path = os.path.join(json_directory, file)
    creation_time = os.path.getctime(file_path)
    creation_time_readable = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
    print(f"{i + 1}: {file} (Creation time: {creation_time_readable})")

# Prompt the user to select files by index
selected_indices_input = input("Enter the indices of the JSON files you want to analyze, separated by commas: ")
selected_indices = [int(index.strip()) - 1 for index in selected_indices_input.split(',') if index.strip().isdigit()]

selected_files = [json_files[i] for i in selected_indices if 0 <= i < len(json_files)]
print(selected_files)

# Technology and other settings inputs
technologies = ["Native", "DLSS", "XeSS", "FSR"]
upscaling_setting = ["None", "Performance", "Balanced", "Quality"]
graphics_settings = ["Low", "Medium", "High"]
resolution = ["1080p", "1440p"]
graphics_card = ["3060", "4060"]

print(f"Select the technology ({', '.join([f'{i}: {tech}' for i, tech in enumerate(technologies)])}): ")
tech_index = int(input())
print(
    f"Select the upscaling setting ({', '.join([f'{i}: {setting}' for i, setting in enumerate(upscaling_setting)])}): ")
upscaling_index = int(input())
print(
    f"Select the graphics setting ({', '.join([f'{i}: {setting}' for i, setting in enumerate(graphics_settings)])}): ")
graphics_index = int(input())
print(f"Select the resolution ({', '.join([f'{i}: {res}' for i, res in enumerate(resolution)])}): ")
resolution_index = int(input())
print(f"Select the graphics card ({', '.join([f'{i}: {gpu}' for i, gpu in enumerate(graphics_card)])}): ")
graphics_card_index = int(input())

for selected_file in selected_files:
    json_file_path = os.path.join(json_directory, selected_file)
    game_name = selected_file.split('-')[1].replace('.exe', '')
    if game_name == "cod":
        game_name = "Modern Warfare III"

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        frame_times = data["Runs"][0]["CaptureData"]["MsBetweenPresents"]

    df = pd.DataFrame(frame_times, columns=["FrameTime"])

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]  # Including milliseconds and trimming to 3 digits
    output_directory = r"C:\Users\Christoph\Documents\Master Thesis\Frametimes"
    output_file_name = f"benchmark_{game_name}_{timestamp}_{technologies[tech_index]}_{upscaling_setting[upscaling_index]}_{graphics_settings[graphics_index]}_{resolution[resolution_index]}_{graphics_card[graphics_card_index]}.xlsx"

    output_file_path = os.path.join(output_directory, output_file_name)
    df.to_excel(output_file_path, index=True)
    print(f"DataFrame saved to {output_file_path}")
