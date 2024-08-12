import os
import pandas as pd

# Define the path to the data folder
data_folder = 'data'
# create the brick_folder if non-existent under Tox24
brick_folder = 'brick'
# Create the 'brick' folder if it doesn't exist
os.makedirs(brick_folder, exist_ok=True)

# Loop through each file in the data folder
for file_name in os.listdir(data_folder):
    if file_name.endswith('.csv'):
        # Construct full file path
        csv_file_path = os.path.join(data_folder, file_name)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Construct the output Parquet file path in the 'brick' subfolder
        parquet_file_path = os.path.join(brick_folder, file_name.replace('.csv', '.parquet'))
        
        # Save the DataFrame as a Parquet file
        df.to_parquet(parquet_file_path, engine='pyarrow')
        
        print(f"Converted {csv_file_path} to {parquet_file_path}")

print("All CSV files have been converted to Parquet format and saved in the 'brick' subfolder.")

