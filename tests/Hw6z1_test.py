import pytest
import random

from Hw6z1 import YandexDisk
from dz1 import FindCityFunc


@pytest.mark.parametrize("x, expected", [("Москва", "Москва"), ("Тула", "Тула")])
def test_cities_check(x, expected):
    result = FindCityFunc(x)
    assert isinstance(result, list)
    for item in result:
        for x in item.values():
            assert expected in x

@pytest.mark.parametrize("x, expected", [("1", 201), ("2", 201), ("1", 409)])
def test_yd_create_folder(x, expected):
    with open("../.token", "r") as f:
        token = f.readline().strip()
    x_res = YandexDisk(token)
    assert expected == x_res.CreateFolder("api_test/test_folder_" + str(x))

