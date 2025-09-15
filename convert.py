# convert.py
import pandas as pd
import os
import sys

def main():
    # find first .xlsm file
    files = [f for f in os.listdir('.') if f.endswith('.xlsm')]
    if not files:
        print("❌ No .xlsm file found in repository root.")
        sys.exit(1)

    file = files[0]
    print(f"Processing {file} ...")

    # Read first sheet (change sheet_name="Sheet1" if needed)
    df = pd.read_excel(file, engine="openpyxl")

    # Save as CSV and JSON
    df.to_csv("data.csv", index=False)
    df.to_json("data.json", orient="records", indent=2, force_ascii=False)

    print("✅ Converted to data.csv and data.json")

if __name__ == "__main__":
    main()
