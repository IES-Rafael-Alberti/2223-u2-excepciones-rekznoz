from src.main5 import verificar_pass
import pytest

def test_verificar_pass():
    with pytest.raises(NameError):
        verificar_pass("pass321")