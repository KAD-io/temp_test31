import pytest

from calculator import Calc


@pytest.mark.unittests
@pytest.mark.add
def test_add_calc():
    assert Calc.adds(2, 3) == 5


@pytest.mark.unittests
@pytest.mark.div
def test_div_calc():
    assert Calc.divides(4, 2) == 2
