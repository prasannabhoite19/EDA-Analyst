import pandas as pd
from typing import Any

class DataLoaderTool:
    def __init__(self):
        self.df = None

    def load_csv(self, path: str) -> str:
        self.df = pd.read_csv(path)
    
    def get_dataframe(self):
        return self.df
    
    def run_eda(self) -> str:
        if self.df is None:
            return "No data loaded."
        
        print(self.df.head())

        eda_report = []
        
        eda_report.append(f"Shape of Dataset: {self.df.shape}")
        
        eda_report.append(f"\nColumn data types:\n{self.df.dtypes}")

        missing = self.df.isnull().sum()
        eda_report.append(f"\nMissing values before filling:\n{missing}")

        num_cols = self.df.select_dtypes(include='number').columns
        cat_cols = self.df.select_dtypes(include='object').columns

        for col in num_cols:
            if self.df[col].isnull().sum() > 0:
                self.df[col].fillna(self.df[col].mean(),inplace=True)
        
        for col in cat_cols:
            if self.df[col].isnull().sum() > 0:
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)

        
        eda_report.append(f"\nMissing values after filling:\n{self.df.isnull().sum()}")

        eda_report.append(f"\nStatistical Summary:\n{self.df.describe(include='all')}")

        eda_report.append(f"\nUnique values per column:\n{self.df.nunique()}")

        numeric_df = self.df.select_dtypes(include='number')
        
        categoric_df = self.df.select_dtypes(include='object')

        return "\n\n".join(eda_report)
    

