import pandas as pd
from src.file_reader_base import FileReader

class CSVReader(FileReader):
    def read(self):
        try:
            df = pd.read_csv(self.file_path)
            return {
                "type": "CSV",
                "rows": len(df),
                "columns": list(df.columns)
            }
        except Exception as e:
            return {"error": str(e)}