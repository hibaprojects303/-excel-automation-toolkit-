import pandas as pd
import os

# folder path (change this)
folder_path = "excel_files"

# get all excel files
files = [f for f in os.listdir(folder_path) if f.endswith(".xlsx")]

all_data = []

for file in files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_excel(file_path)
    all_data.append(df)

# merge all data
merged_df = pd.concat(all_data, ignore_index=True)

# save output
merged_df.to_excel("merged_output.xlsx", index=False)

print("All files merged successfully!")