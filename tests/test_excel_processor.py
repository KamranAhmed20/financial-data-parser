import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from core.excel_processor import ExcelProcessor

class TestExcelProcessor(unittest.TestCase):
    def test_load_excel_file(self):
        processor = ExcelProcessor()
        file_path = os.path.join("data", "sample", "KH_Bank.XLSX")
        processor.load_files([file_path])
        self.assertIn(file_path, processor.data)

if __name__ == "__main__":
    unittest.main()
