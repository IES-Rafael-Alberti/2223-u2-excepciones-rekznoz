from src.main4 import strisdigit
import pytest

def test_edad():
    with pytest.raises(ValueError):
        strisdigit("ASDASD")