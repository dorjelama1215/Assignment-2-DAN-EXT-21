import os
import pandas as pd
import numpy as np


def load_temperature_data(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' not found.")

    all_data = []
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder_path, file))
            all_data.append(df)

    if not all_data:
        raise ValueError("No CSV files found in the temperatures folder.")

    return pd.concat(all_data, ignore_index=True)


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
    df["Season"] = df["Date"].dt.month.apply(get_season)
    return df


def save_seasonal_averages(df, output_file="average_temp.txt"):
    seasonal_avg = df.groupby("Season")["Temperature"].mean()
    order = ["Summer", "Autumn", "Winter", "Spring"]

    with open(output_file, "w") as f:
        for season in order:
            if season in seasonal_avg:
                f.write(f"{season}: {seasonal_avg[season]:.1f}°C\n")


def save_largest_temperature_range(df, output_file="largest_temp_range_station.txt"):
    stats = df.groupby("Station")["Temperature"].agg(["max", "min"])
    stats["range"] = stats["max"] - stats["min"]

    max_range = stats["range"].max()
    largest_range_stations = stats[stats["range"] == max_range]

    with open(output_file, "w") as f:
        for station, row in largest_range_stations.iterrows():
            f.write(
                f"Station {station}: Range {row['range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
            )


def save_temperature_stability(df, output_file="temperature_stability_stations.txt"):
    std_dev = df.groupby("Station")["Temperature"].std()

    min_std = std_dev.min()
    max_std = std_dev.max()

    most_stable = std_dev[std_dev == min_std]
    most_variable = std_dev[std_dev == max_std]

    with open(output_file, "w") as f:
        for station, value in most_stable.items():
            f.write(f"Most Stable: Station {station}: StdDev {value:.1f}°C\n")

        for station, value in most_variable.items():
            f.write(f"Most Variable: Station {station}: StdDev {value:.1f}°C\n")

    print(f"Temperature stability results saved to {output_file}")


def main():
    df = load_temperature_data("temperatures")
    df = clean_data(df)
    df = add_season_column(df)

    save_seasonal_averages(df)
    save_largest_temperature_range(df)
    save_temperature_stability(df)

if __name__ == "__main__":
    main()
