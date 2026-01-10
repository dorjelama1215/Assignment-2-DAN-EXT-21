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
    return df.dropna(subset=["Temperature"])


def get_season(month):
    if month in [12, 1, 2]:
        return "Summer"
    elif month in [3, 4, 5]:
        return "Autumn"
    elif month in [6, 7, 8]:
        return "Winter"
    else:
        return "Spring"


def add_season_column(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month
    df["Season"] = df["Month"].apply(get_season)
    return df


def main():
    folder_path = "temperatures"
    
   
    df = load_temperature_data(folder_path)
    df = clean_data(df)
    
    print("After cleaning NaN values (first 5 rows):")
    print(df.head())

   
    df = add_season_column(df)
    print("\nAfter adding Season column (first 5 rows):")
    print(df.head())

if __name__ == "__main__":
    main()
