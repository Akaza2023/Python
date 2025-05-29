from src.csv_reader import CSVReader
from src.json_reader import JSONReader
from src.txt_reader import TXTReader
from src.report_generator import ReportGenerator
import logging

logging.basicConfig(
    level = logging.INFO,
    format="%(levelname)s: %(message)s"
)
report = ReportGenerator()

# created a report object, I think we gona use to gen

file_readers = [
    CSVReader("data/sample_csv.csv"),
    JSONReader("data/sample_json.json"),
    TXTReader("data/sample_txt.txt")
]


for reader in file_readers:
    try:
        result = reader.read()
    except Exception as e:
        logging.error(f"Failed to read {reader.file_path}: {str(e)}")
        report.add_line(f"Error reading {reader.file_path} : {str(e)}")

    if "error" in result:
        report.add_line(f"{result['type']} File: {reader.file_path}")
        report.add_line(f"  ❌ Error: {result['error']}")
        continue

    if result["type"] == "CSV" or result["type"] == "JSON":
        report.add_line(f"{result['type']} File: {reader.file_path}")
        report.add_line(f"  ➤ Rows: {result['rows']}")
        report.add_line(f"  ➤ Columns: {', '.join(result['columns'])}")
    elif result["type"] == "TXT":
        report.add_line(f"{result['type']} File: {reader.file_path}")
        report.add_line(f"  ➤ Lines: {result['lines']}")

    report.add_line("")  # Empty line for spacing

# 4. Save the final summary
report.save("output/summary.txt")
logging.info("✅ Summary report generated at: output/summary.txt")

