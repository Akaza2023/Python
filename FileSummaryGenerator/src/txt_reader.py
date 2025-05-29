from src.file_reader_base import FileReader

class TXTReader(FileReader):
    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                lines = f.readlines()
            return {
                "type": "TXT",
                "lines": len(lines)
            }
        except Exception as e:
            return {"error": str(e)}
    