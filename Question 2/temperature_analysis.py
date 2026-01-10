import os
import pandas as pd
import numpy as np

def load_temperatures_data(folder_path):
    all_data = []

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path)
            all_data.append(df)

    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df

def main():
    df = load_temperatures_data("temperatures")
    print(df.head())

if __name__ == "__main__":
    main()
