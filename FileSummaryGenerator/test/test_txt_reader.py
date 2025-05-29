from src.txt_reader import TXTReader

def test_txt_reader_success():
    reader = TXTReader('data/sample_txt.txt')
    result = reader.read()
    assert result['type'] == 'TXT'
    assert result["lines"] == 3