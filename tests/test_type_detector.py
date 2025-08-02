import unittest
import pandas as pd
from core.type_detector import DataTypeDetector

class TestTypeDetector(unittest.TestCase):
    def test_detect_number_column(self):
        detector = DataTypeDetector()
        series = pd.Series([100, 200, 300])
        dtype, _ = detector.detect_column_type(series)
        self.assertEqual(dtype, "number")

if __name__ == "__main__":
    unittest.main()
