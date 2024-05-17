# Q.1 Write a program to read data from a CSV file and perform basic data cleaning operations like removing duplicates or handling missing values.

import pandas as pd

def clean_csv(file_path):
    df = pd.read_csv(file_path)
    df.drop_duplicates(inplace=True)
    df.fillna("Missing", inplace=True)
    return df

# Example usage
file_path = 'data.csv'
cleaned_data = clean_csv(file_path)
print(cleaned_data)
