# 🧾 File Summary Generator (OOP Mini Project)

A Python-based mini project demonstrating **Object-Oriented Programming**, clean project structure, and file operations using CSV, JSON, and TXT readers. Generates a clean summary report from structured file inputs.

---

## 📌 Features
- ✅ OOP design with base/derived classes
- ✅ Reads `.csv`, `.json`, and `.txt` files
- ✅ Generates a summary report
- ✅ Logging, error handling, and unit testing
- ✅ Modular, extensible, and GitHub-ready

---

## 🧠 Tech Stack
- Python 3.10+
- Logging (built-in)
- `unittest` for testing

---

## 🗂️ Folder Structure
roject_root/
│
├── src/                    # Source code
│   ├── base_reader.py
│   ├── csv_reader.py
│   ├── json_reader.py
│   ├── txt_reader.py
│   └── main.py
│
├── data/                   # Input sample files
│   ├── sample.csv
│   ├── sample.json
│   └── sample.txt
│
├── test/                   # Unit tests
│   ├── csv_reader_test.py
│   ├── json_reader_test.py
│   └── txt_reader_test.py
│
├── output/                 # Generated summary reports
│   └── summary.txt
│
├── requirements.txt
├── README.md
└── .gitignore

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the main script:
    python src/main.py

3. Run tests:
    pytest

Sample Output:

File Summary Report

TXT File:
- Lines: 20
- Words: 230

CSV File:
- Rows: 30
- Columns: 5

JSON File:
- Records: 50

🙌 Author

Built with ❤️ by Aditya as part of mastering Python + OOP foundations.