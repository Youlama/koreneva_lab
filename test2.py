from modify_levenstain import levenstain

import pytest
def test_empty():
    assert levenstain("", "пустыня") ==  7
def test_equal():
    assert levenstain("пустыня", "пустыня") == 0
def test_differ():
    assert levenstain("ложка","лодка") == 1

if __name__ == '__main__':
    pytest.main()