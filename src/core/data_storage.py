import pandas as pd

class FinancialDataStore:
    def __init__(self):
        self.datasets = {}
        self.column_types = {}

    def add_dataset(self, name, df, types):
        self.datasets[name] = df
        self.column_types[name] = types
        print(f"Dataset '{name}' added with {len(df)} rows and {len(df.columns)} columns.")

    def query_by_criteria(self, name, **filters):
        if name not in self.datasets:
            print(f"Dataset '{name}' not found.")
            return None

        df = self.datasets[name]
        for col, value in filters.items():
            if col not in df.columns:
                continue
            if isinstance(value, tuple) and len(value) == 2:
                df = df[(df[col] >= value[0]) & (df[col] <= value[1])]
            else:
                df = df[df[col] == value]

        print(f"Query returned {len(df)} rows.")
        return df

    def aggregate_data(self, name, group_by, agg_column, agg_func='sum'):
        if name not in self.datasets:
            print(f"Dataset '{name}' not found.")
            return None

        df = self.datasets[name]
        if group_by not in df.columns or agg_column not in df.columns:
            return None

        grouped = df.groupby(group_by)[agg_column].agg(agg_func)
        return grouped.reset_index()
