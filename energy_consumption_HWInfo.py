import pandas as pd
import datetime
import os
from datetime import datetime

csv_directory = r'C:\Program Files\HWiNFO64'


# Function to list all CSV files and load the selected one


def list_and_select_csv(csv_directory):
    csv_files_with_dates = [(file, os.path.getctime(os.path.join(csv_directory, file))) for file in
                            os.listdir(csv_directory) if file.endswith('.CSV')]

    # Check if there are any CSV files in the directory
    if not csv_files_with_dates:
        print("No CSV files found in the directory.")
        return

    # Sort files by creation date, newest first
    csv_files_with_dates.sort(key=lambda x: x[1], reverse=True)

    # Display the list of available CSV files with their creation dates
    print("Available CSV files:")
    for i, (file, ctime) in enumerate(csv_files_with_dates):
        date_str = datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{i + 1}: {file} (Created: {date_str})")

    # Ask the user to select a file
    selection = int(input("Enter the number of the CSV file you want to analyze: ")) - 1
    if selection < 0 or selection >= len(csv_files_with_dates):
        print("Invalid selection.")
        return

    selected_file_path = os.path.join(csv_directory, csv_files_with_dates[selection][0])

    # Load the selected CSV file

    data = pd.read_csv(selected_file_path, usecols=['Date', 'Time', 'GPU Core Load [%]', 'GPU Power (Total) [W]'],
                       encoding='cp1252')
    data = data.iloc[:-2]
    return data


# Creation of the Data Frame

df = pd.DataFrame(list_and_select_csv(csv_directory))

# Convert 'GPU Core Load [%]' and 'GPU Power (Total) [W]' columns to numeric
df['GPU Core Load [%]'] = pd.to_numeric(df['GPU Core Load [%]'], errors='coerce')
df['GPU Power (Total) [W]'] = pd.to_numeric(df['GPU Power (Total) [W]'], errors='coerce')

now = datetime.now()
timestamp = now.strftime("%m_%d_%H_%M_%S")  # Example: "10_30_11_44_59"


def check_benchmark():
    games = ["Call of Duty MW III", "Cyberpunk 2077", "AC Mirage", "Diablo IV", "The Witcher 3"]
    technologies = ["Native", "DLSS", "XeSS", "FSR"]
    upscaling_setting = ["None", "Performance", "Balanced", "Quality"]
    graphics_settings = ["Low", "Medium", "High"]
    resolution = ["1080p", "1440p"]
    graphics_card = ["3060", "4060"]
    game_index = int(input(f"Select the game ({', '.join([f'{i}: {tech}' for i, tech 
                                                          in enumerate(games)])}): "))
    tech_index = int(input(f"Select the technology ({', '.join([f'{i}: {tech}' for i, tech 
                                                                in enumerate(technologies)])}): "))
    upscaling_index = int(input(f"Select the upscaling setting ({', '.join([f'{i}: {setting}' for i, setting
                                                                            in enumerate(upscaling_setting)])}): "))
    graphics_index = int(input(f"Select the graphics setting ({', '.join([f'{i}: {setting}' for i, setting 
                                                                          in enumerate(graphics_settings)])}): "))
    resolution_index = int(input(f"Select the resolution ({', '.join([f'{i}: {res}' for i, res 
                                                                      in enumerate(resolution)])}): "))
    graphics_card_index = int(input(f"Select the graphics card ({', '.join([f'{i}: {gpu}' for i, gpu
                                                                      in enumerate(graphics_card)])}): "))
    game_name = games[game_index]
    technology_name = technologies[tech_index]
    upscaling_name = upscaling_setting[upscaling_index]
    graphis_name = graphics_settings[graphics_index]
    resolution_name = resolution[resolution_index]
    graphis_card_name = graphics_card[graphics_card_index]
    return game_name, technology_name, upscaling_name, graphis_name, resolution_name, graphis_card_name


game_name, technology_name, upscaling_name, graphis_name, resolution_name, graphis_card_name = check_benchmark()

output_directory = r"C:\Users\Christoph\Documents\Master Thesis\Energy Consumption"
output_file_name = (f"Energy_Consumption_{game_name}_{technology_name}_{upscaling_name}_{graphis_name}_"
                    f"{resolution_name}_{timestamp}_{graphis_card_name}.xlsx")

output_file_path = os.path.join(output_directory, output_file_name)

# Save the DataFrame to Excel
df.to_excel(output_file_path, index=False)

print(f"DataFrame saved to {output_file_path}")
