from src.main2 import numeros_impares
import pytest

def test_numeros_impares():
    with pytest.raises(ValueError):
        numeros_impares(-9)