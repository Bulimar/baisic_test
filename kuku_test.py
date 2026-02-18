import pytest
import array
from main import compress_numbers 

class TestCompressNumbers:
    
    @pytest.mark.parametrize("input_data, expected", [
        (array.array('i', [1, 2, 2, 4]), array.array('i', [1, 2, 4])),
        (array.array('i', [0, 0, 1, 1, 0]), array.array('i', [0, 1, 0])),
        (array.array('i', [42]), array.array('i', [42])),
        (array.array('i', [-1, 1, 1, -1, -1]), array.array('i', [-1, 1, -1])),
        (array.array('d', [1.1, 1.1, 2.2, 2.2, 3.3]), array.array('d', [1.1, 2.2, 3.3])),
        (array.array('u', ['h', 'e', 'l', 'l', 'o']), array.array('u', ['h', 'e', 'l', 'o']))

    ])
    def test_compress(self, input_data, expected):
        result = compress_numbers(input_data)
        assert result == expected

    def test_nal(self):
        result = compress_numbers(array.array('i', [])) 
        rav =  array.array('i', [])
        assert result == rav
