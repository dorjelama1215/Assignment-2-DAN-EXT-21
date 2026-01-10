import os
import pandas as pd
import numpy as np


def load_temperature_data(folder_path):
   
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' not found.")

    all_data = []

   
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            all_data.append(df)

    if not all_data:
        raise ValueError("No CSV files found in the temperatures folder.")

    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def clean_data(df):
    """
    Removes rows where Temperature is NaN.
    Returns a cleaned DataFrame.
    """
    cleaned_df = df.dropna(subset=["Temperature"])
    return cleaned_df


def main():
    folder_path = "temperatures"  
    df = load_temperature_data(folder_path)
    print("Loaded data (first 5 rows):")
    print(df.head())

 
    df = clean_data(df)
    print("\nAfter cleaning NaN values (first 5 rows):")
    print(df.head())

if __name__ == "__main__":
    main()
