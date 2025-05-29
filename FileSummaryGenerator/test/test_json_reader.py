from src.json_reader import JSONReader

def test_json_reader_success():
    reader = JSONReader('data/sample_json.json')
    result = reader.read()
    assert result['type'] == 'JSON'
    assert result['rows'] == 3
    assert "id" in result["columns"]
