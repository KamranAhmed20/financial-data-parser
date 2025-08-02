from dateutil.parser import parse
import pandas as pd
import numpy as np

class DataTypeDetector:
    def detect_column_type(self, column_data):
        non_null = column_data.dropna()
        total = len(non_null)
        if total == 0:
            return "unknown", 0.0

        date_count = 0
        number_count = 0

        for val in non_null:
            if self.is_date(val):
                date_count += 1
            elif self.is_number(val):
                number_count += 1

        date_confidence = date_count / total
        number_confidence = number_count / total
        string_confidence = 1.0 - max(date_confidence, number_confidence)

        if date_confidence > 0.8:
            return "date", date_confidence
        elif number_confidence > 0.8:
            return "number", number_confidence
        else:
            return "string", string_confidence

    def is_date(self, value):
        try:
            if isinstance(value, (pd.Timestamp, np.datetime64)):
                return True

            s = str(value)
            if s.isdigit() and len(s) <= 4:
                return False

            parse(s, fuzzy=False)
            return True
        except:
            return False

    def is_number(self, value):
        try:
            float(str(value).replace(",", "").replace("(", "-").replace(")", ""))
            return True
        except:
            return False
