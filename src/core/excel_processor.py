import pandas as pd
import os

class ExcelProcessor:
    def __init__(self):
        self.data = {}  # file_path -> {sheet_name: dataframe}

    def load_files(self, file_paths):
        for file_path in file_paths:
            try:
                sheets = pd.read_excel(file_path, sheet_name=None, engine='openpyxl')
                self.data[file_path] = sheets
                print(f"Loaded {len(sheets)} sheets from {os.path.basename(file_path)}")
            except Exception as e:
                print(f"Failed to load {file_path}: {e}")

    def get_sheet_info(self):
        for file_path, sheets in self.data.items():
            print(f"\nFile: {os.path.basename(file_path)}")
            for sheet_name, df in sheets.items():
                print(f"  Sheet: {sheet_name}")
                print(f"    Rows: {df.shape[0]}, Columns: {df.shape[1]}")
                print(f"    Columns: {list(df.columns)}")
