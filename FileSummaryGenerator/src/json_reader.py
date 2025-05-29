import json
import pandas as pd
from src.file_reader_base import FileReader

class JSONReader(FileReader):
    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            df = pd.DataFrame(data)
            return {
                "type": "JSON",
                "rows": len(df),
                "columns": list(df.columns)
            }
        except Exception as e:
            return {"error": str(e)}