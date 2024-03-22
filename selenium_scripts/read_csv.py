import os
import pandas as pd
import json
from pandas.api.types import infer_dtype

def generate_column_info(csv_folder, json_path):
    # Initialize an empty dictionary to store column information
    column_info = {}

    # If the JSON file already exists, load its content
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as existing_json:
            column_info = json.load(existing_json)

    # Iterate over all CSV files in the folder
    for filename in os.listdir(csv_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(csv_folder, filename)

            # Read the CSV file with UTF-8 encoding
            df = pd.read_csv(file_path, encoding='utf-8')

            # Update column information for each file
            for column in df.columns:
                if column not in column_info:
                    # Use infer_dtype to get the most specific Python data type for each column
                    data_type = infer_dtype(df[column])
                    column_info[column] = {
                        "data_type": data_type,
                        "null_count": 0,
                        "unique_count": 0,
                        "top_value": "",
                        "top_value_count": 0,
                    }

                # Update column information based on the current file
                column_info[column]["null_count"] += int(df[column].isnull().sum())
                column_info[column]["unique_count"] += int(df[column].nunique())

                # Update top value and top value count if applicable
                value_counts = df[column].value_counts()
                if not value_counts.empty:
                    top_value = value_counts.idxmax()
                    top_value_count = int(value_counts.iloc[0])

                    if top_value_count > column_info[column]["top_value_count"]:
                        column_info[column]["top_value"] = str(top_value)
                        column_info[column]["top_value_count"] = top_value_count

    # Save column information to a single JSON file with UTF-8 encoding
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(column_info, json_file, indent=2, ensure_ascii=False)
    print(f"JSON file created/updated successfully: {json_path}")

if __name__ == "__main__":
    # Specify the path to the CSV folder and the desired JSON file
    csv_folder_path = "csv_files"
    json_output_path = "csv_data.json"

    # Call the function to generate column information
    generate_column_info(csv_folder_path, json_output_path)