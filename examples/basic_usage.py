import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from core.excel_processor import ExcelProcessor
from core.type_detector import DataTypeDetector
from core.format_parser import FormatParser
from core.data_storage import FinancialDataStore

def main():
    base_path = os.path.join("data", "sample")
    files = [
        os.path.join(base_path, "KH_Bank.XLSX"),
        os.path.join(base_path, "Customer_Ledger_Entries_FULL.xlsx")
    ]

    processor = ExcelProcessor()
    processor.load_files(files)

    detector = DataTypeDetector()
    parser = FormatParser()
    store = FinancialDataStore()

    for file_path, sheets in processor.data.items():
        for sheet_name, df in sheets.items():
            cleaned_df = pd.DataFrame()
            col_types = {}

            for column in df.columns:
                col_data = df[column]
                col_type, _ = detector.detect_column_type(col_data)
                col_types[column] = col_type

                if col_type == "number":
                    cleaned_df[column] = col_data.apply(parser.parse_amount)
                elif col_type == "date":
                    cleaned_df[column] = col_data.apply(parser.parse_date)
                else:
                    cleaned_df[column] = col_data

            dataset_name = f"{os.path.basename(file_path)}::{sheet_name}"
            store.add_dataset(dataset_name, cleaned_df, col_types)

            # Run a sample query and aggregation if possible
            if "Amount" in cleaned_df.columns:
                result = store.query_by_criteria(dataset_name, Amount=(1000, 1000000))
                if result is not None:
                    print(result.head())

            if "Customer Name" in cleaned_df.columns and "Amount" in cleaned_df.columns:
                summary = store.aggregate_data(dataset_name, "Customer Name", "Amount")
                if summary is not None:
                    print(summary.head())

if __name__ == "__main__":
    main()
