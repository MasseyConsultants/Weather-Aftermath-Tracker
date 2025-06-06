import csv
import os

def check_csv(file_path):
    print(f"\nChecking file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read first 5 lines
            reader = csv.reader(file)
            headers = next(reader)
            print("CSV Headers:", headers)
            print("\nFirst 5 rows:")
            for i, row in enumerate(reader):
                if i >= 5:
                    break
                print(f"Row {i+1}:", row)
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")

if __name__ == "__main__":
    files = [
        'Data/1950-2024_actual_tornadoes.csv',
        'Data/1950-2024_all_tornadoes.csv',
        'Data/2024_hail.csv',
        'Data/2024_wind.csv'
    ]
    
    for file in files:
        if os.path.exists(file):
            check_csv(file)
        else:
            print(f"\nFile not found: {file}") 