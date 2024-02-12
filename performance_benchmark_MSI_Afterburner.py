import os
import pandas as pd
import datetime

benchmark_file = r"C:\Users\Christoph\Documents\Master Thesis\Performance\Benchmark.txt"

def read_file_and_create_dataframe(file_path):
    benchmark_data = []
    game_names = set()  # Use a set to avoid duplicate game names
    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if "benchmark completed" in lines[i]:
                benchmark_info = extract_benchmark_info(lines[i:i+7])
                benchmark_data.append(benchmark_info)
                game_names.add(benchmark_info["Game Name"])  # Add game name to the set
            i += 1
    df = pd.DataFrame(benchmark_data)
    return df, game_names


def extract_benchmark_info(file_lines):
    # Parsing the first line for game name, date, and time
    game_name_line = file_lines[0]
    parts = game_name_line.split(',')
    duration = file_lines[0].split()[-2]+"s"
    date_part= parts[0].strip()
    time_part = file_lines[0].split()[1]
    game_name_part = parts[1].split()[1].strip(".exe")

    # Correctly parsing the benchmark metrics
    average_frame_rate = float(file_lines[1].split(':')[1].strip().split(' ')[0])
    minimum_frame_rate = float(file_lines[2].split(':')[1].strip().split(' ')[0])
    maximum_frame_rate = float(file_lines[3].split(':')[1].strip().split(' ')[0])
    low_1_percent = float(file_lines[4].split(':')[1].strip().split(' ')[0])
    low_0_1_percent = float(file_lines[5].split(':')[1].strip().split(' ')[0])

    return {
        "Game Name": game_name_part,
        "Duration" : duration,
        "Date": date_part,
        "Time": time_part,
        "Average FPS": average_frame_rate,
        "Minimum FPS": minimum_frame_rate,
        "Maximum FPS": maximum_frame_rate,
        "1% low": low_1_percent,
        "0.1% low": low_0_1_percent
    }


df, game_names = read_file_and_create_dataframe(benchmark_file)
game_names = list(game_names)
game_names = game_names[0]
now = datetime.datetime.now()
timestamp = now.strftime("%m_%d_%H_%M")  # Example: "10_30_11_44"

def check_benchmark():

    technologies = ["Native", "DLSS", "XeSS", "FSR"]
    upscaling_setting = ["None", "Performance", "Balanced", "Quality"]
    graphics_settings = ["Low", "Medium", "High"]
    resolution = ["1080p", "1440p"]
    graphics_card = ["3060", "4060"]
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
    technology_name = technologies[tech_index]
    upscaling_name = upscaling_setting[upscaling_index]
    graphis_name = graphics_settings[graphics_index]
    resolution_name = resolution[resolution_index]
    graphis_card_name = graphics_card[graphics_card_index]
    return technology_name, upscaling_name, graphis_name, resolution_name,graphis_card_name


technology_name, upscaling_name, graphis_name, resolution_name, graphis_card_name = check_benchmark()

# Define the target directory and file name
output_directory = r"C:\Users\Christoph\Documents\Master Thesis\Benchmark"

# Now include game_name in your output file name
output_file_name = f"benchmark_{game_names}_{timestamp}_{technology_name}_{upscaling_name}_{graphis_name}_{resolution_name}_{graphis_card_name}.xlsx"

# Full file path
output_file_path = os.path.join(output_directory, output_file_name)

# Save the DataFrame to Excel
df.to_excel(output_file_path, index=False)
