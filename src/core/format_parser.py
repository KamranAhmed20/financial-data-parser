import re
from datetime import datetime
from dateutil import parser
import pandas as pd


class FormatParser:

    def parse_amount(self, value):
        if pd.isna(value):
            return None

        if isinstance(value, (int, float)):
            return float(value)

        # Convert to string
        val_str = str(value).strip().replace("₹", "").replace("$", "").replace("€", "").replace(",", "")

        # Handle negative with parentheses
        if val_str.startswith("(") and val_str.endswith(")"):
            val_str = "-" + val_str[1:-1]

        # Handle suffix multipliers
        match = re.match(r"([\d.]+)([KkMmBb])", val_str)
        if match:
            num, suffix = match.groups()
            factor = {"K": 1e3, "M": 1e6, "B": 1e9}
            return float(num) * factor[suffix.upper()]

        try:
            return float(val_str)
        except:
            return None

    def parse_date(self, value):
        if pd.isna(value):
            return None

        # Excel serial date (usually > 40000)
        try:
            if isinstance(value, (int, float)) and value > 40000:
                return datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(value) - 2)
        except:
            pass

        # Try standard date parsing
        try:
            return parser.parse(str(value), fuzzy=True)
        except:
            return None
