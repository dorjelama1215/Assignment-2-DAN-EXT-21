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


def save_seasonal_averages(df, output_file="average_temp.txt"):
    seasonal_avg = df.groupby("Season")["Temperature"].mean()

 
    seasons_order = ["Summer", "Autumn", "Winter", "Spring"]

    with open(output_file, "w") as f:
        for season in seasons_order:
            if season in seasonal_avg:
                f.write(f"{season}: {seasonal_avg[season]:.1f}°C\n")

    print(f"Seasonal averages saved to {output_file}")


def main():
    folder_path = "temperatures"
    
    df = load_temperature_data(folder_path)
    df = clean_data(df)
    df = add_season_column(df)

    
    save_seasonal_averages(df)

    print("Data after adding Season column (first 5 rows):")
    print(df.head())

if __name__ == "__main__":
    main()
