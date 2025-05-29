# from src.csv_reader import CSVReader
# from src.json_reader import JSONReader
# from src.txt_reader import TXTReader

# csv_reader = CSVReader('data/sample_csv.csv')
# json_reader = JSONReader('data/sample_json.json')
# txt_reader = TXTReader('data/sample_txt.txt')

# csv_result = csv_reader.read()
# json_result = json_reader.read()
# txt_result = txt_reader.read()

# print("CSV: ", csv_result)
# print("JSON: ", json_result)
# print("TXT: ", txt_result) 

from src.report_generator import ReportGenerator

report = ReportGenerator()
report.add_line("CSV File: sample_csv.csv")
report.add_line("  ➤ Rows: 3")
report.add_line("  ➤ Columns: id, name, age")
report.add_line("JSON File: sample_json.json")
report.add_line("  ➤ Rows: 3")
report.add_line("  ➤ Columns: id, city")
report.add_line("TXT File: sample_txt.txt")
report.add_line("  ➤ Lines: 3")

report.save("output/summary.txt")
