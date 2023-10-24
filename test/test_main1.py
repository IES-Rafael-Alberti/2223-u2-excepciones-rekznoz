from src.main1 import verificar_edad
import pytest

def test_edad():
    with pytest.raises(ValueError):
        verificar_edad(-5)