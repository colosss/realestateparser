import pytest

from src.main import Calculator

@pytest.mark.parametrize(
    "x, y, rez",
    [
        (1, 2, 3),
        (1, -1, 0),
    ]
)
def test_add (x, y, rez):
    assert Calculator().add(x, y) == rez