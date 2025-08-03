# Financial Data Parser

A robust Excel financial data parser that automatically detects column types, normalizes messy formats, and provides fast querying capabilities for financial data analysis.

## Features

- **Excel Processing**: Reads `.xlsx` files with multiple sheets
- **Type Detection**: Auto-detects string, number, and date columns with confidence scores
- **Format Parsing**: Handles various amount formats ($1,234.56, €1.234,56, 1.5M) and date formats
- **Data Storage**: Efficient filtering, range queries, and aggregation using pandas
- **Unit Tests**: Comprehensive test coverage for core functionality

## Project Structure

```
financial-data-parser/
├── data/
│   └── sample/              # Sample Excel files
├── examples/
│   └── basic_usage.py       # Main demo
├── src/
│   └── core/                # Core modules
│       ├── excel_processor.py
│       ├── type_detector.py
│       ├── format_parser.py
│       └── data_storage.py
├── tests/                   # Unit tests
├── requirements.txt
└── README.md
```

## How to Run This Project

### 1. Setup Environment

```bash
git clone https://github.com/KamranAhmed20/financial-data-parser.git
cd financial-data-parser
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### 2. Run Demo

```bash
python examples/basic_usage.py
```

### 3. Run Tests

```bash
python -m unittest discover -s tests -v
```

## Usage Example

```python
from src.core.excel_processor import ExcelProcessor
from src.core.data_storage import DataStorage

# Load and process Excel file
processor = ExcelProcessor()
storage = DataStorage()

file_info = processor.load_excel("data/sample/financial_data.xlsx")
for sheet_name, sheet_data in file_info.sheets.items():
    processed_data = processor.process_sheet(sheet_data)
    storage.store_data(f"{file_info.filename}::{sheet_name}", processed_data)

# Query data
results = storage.query_by_criteria(
    "financial_data.xlsx::Sheet1", 
    Amount=(1000, 100000)
)
```

## Requirements

```
pandas>=1.5.0
openpyxl>=3.0.0
python-dateutil>=2.8.0
numpy>=1.21.0
```

## Author

**Kamran Ahmed**  
AI & Software Development | Air University  
📧 kamranahmed7602@gmail.com  
🌐 github.com/KamranAhmed20
