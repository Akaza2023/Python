from src.csv_reader import CSVReader

def test_csv_reader_success():
    reader = CSVReader('data/sample_csv.csv')
    result = reader.read()
    assert result['type'] == 'CSV'
    assert result['rows'] == 3
    assert "name" in result["columns"]
