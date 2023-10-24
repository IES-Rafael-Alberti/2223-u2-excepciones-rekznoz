from src.main3 import cuenta_atras
import pytest

def test_cuenta_atras():
    with pytest.raises(ValueError):
        cuenta_atras(-9)