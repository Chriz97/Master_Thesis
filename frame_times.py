import json
import pandas as pd
import datetime
import os

# Define the file path
json_file_path = r'C:\Users\Christoph\Documents\CapFrameX\Captures\CapFrameX-BlackOps.exe-2023-10-30T233443.json'

# Open and read the JSON file
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

# Define the target directory and file name
output_directory = r"C:\Users\Christoph\Documents\Master Thesis\Frametimes"
output_file_name = f"benchmark_{timestamp}.xlsx"

# Full file path
output_file_path = os.path.join(output_directory, output_file_name)

# Save the DataFrame to Excel
df.to_excel(output_file_path, index=True)

print(f"DataFrame saved to {output_file_path}")







