import os
import pandas as pd
import datetime

benchmark_file = r"C:\Program Files (x86)\MSI Afterburner\Benchmark.txt"

def read_file_and_create_dataframe(file_path):
    benchmark_data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            if "benchmark completed" in lines[i]:
                benchmark_data.append(extract_benchmark_info(lines[i:i+7]))
            i += 1

    df = pd.DataFrame(benchmark_data)
    return df


def extract_benchmark_info(file_lines):
    game_name_line = file_lines[0]
    game_name_parts = game_name_line.split(',')[1].split("benchmark completed")[0].strip().split()
    game_name = game_name_parts[-1].split('.')[0]  # Take the last part and remove the extension if present
    if game_name == "cod":
        game_name = "Modern Warfare" # Change "cod" to "Modern Warfare"
    print(game_name)
    date = game_name_line.split(',')[0].split("benchmark completed")[0].strip()
    time = game_name_line.split(',')[1].split("benchmark completed")[0].strip().split()[0]
    average_frame_rate = float(file_lines[2].split(":")[1].strip().split()[0])
    low_1_percent = float(file_lines[4].split(":")[1].strip().split()[0])
    low_0_1_percent = float(file_lines[5].split(":")[1].strip().split()[0])

    return {
        "Game Name": game_name,
        "Date": date,
        "Time": time,
        "Average FPS": average_frame_rate,
        "1% low": low_1_percent,
        "0.1% low": low_0_1_percent
    }

df = read_file_and_create_dataframe(benchmark_file)

now = datetime.datetime.now()
timestamp = now.strftime("%m_%d_%H_%M")  # Example: "10_30_11_44"

# Define the target directory and file name
output_directory = r"C:\Users\Christoph\Documents\Master Thesis\Benchmark"
output_file_name = f"benchmark_{timestamp}.xlsx"

# Full file path
output_file_path = os.path.join(output_directory, output_file_name)

# Save the DataFrame to Excel
df.to_excel(output_file_path, index=False)

#print(f"DataFrame saved to {output_file_path}")
print(df)
