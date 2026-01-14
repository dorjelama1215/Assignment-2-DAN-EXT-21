import os
import pandas as pd


def load_temperature_data(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' not found.")

    csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
    if not csv_files:
        raise ValueError("No CSV files found in the temperatures folder.")
 # Get all CSV files in the folder
    all_data = []
   
    for file in csv_files:
        df = pd.read_csv(os.path.join(folder_path, file))
        all_data.append(df)

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

# Calculates average temperature for each season and save the result at average_temp.txt

def save_seasonal_averages(df, output_file="average_temp.txt"):
    seasonal_avg = df.groupby("Season")["Temperature"].mean()
    order = ["Summer", "Autumn", "Winter", "Spring"]

    with open(output_file, "w") as f:
        for season in order:
            if season in seasonal_avg:
                f.write(f"{season}: {seasonal_avg[season]:.1f}°C\n")

# finding the station with highest temperature rnge

def save_largest_temperature_range(df, output_file="largest_temp_range_station.txt"):
    stats = df.groupby("Station")["Temperature"].agg(["max", "min"])
    stats["range"] = stats["max"] - stats["min"]

    max_range = stats["range"].max()
    largest = stats[stats["range"] == max_range]

    with open(output_file, "w") as f:
        for station, row in largest.iterrows():
            f.write(
                f"Station {station}: Range {row['range']:.1f}°C "
                f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n"
            )

# Calculating temp stability using standard deviation 

def save_temperature_stability(df, output_file="temperature_stability_stations.txt"):
    std_dev = df.groupby("Station")["Temperature"].std()

 
 # Identifing smallest and largest standard deviation
 
    min_std = std_dev.min()
    max_std = std_dev.max()

    with open(output_file, "w") as f:
        for station, value in std_dev[std_dev == min_std].items():
            f.write(f"Most Stable: Station {station}: StdDev {value:.1f}°C\n")

        for station, value in std_dev[std_dev == max_std].items():
            f.write(f"Most Variable: Station {station}: StdDev {value:.1f}°C\n")


def main():
    df = load_temperature_data("temperatures")
    df = clean_data(df)
    df = add_season_column(df)

    save_seasonal_averages(df)
    save_largest_temperature_range(df)
    save_temperature_stability(df)

    print("✅ Temperature analysis completed successfully.")

if __name__ == "__main__":
    main()
