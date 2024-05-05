import pytest

from challenge_001.celsius_model import CelsiusModel
from challenge_001.challenge_001 import celsius_to_fahrenheit, multiple_number
from challenge_001.fahrenheit_model import FahrenheitModel


@pytest.mark.parametrize(
    "cercius_list, expected_data",
    [
        ([CelsiusModel(temperature=0.0)], [FahrenheitModel(temperature=32.0)]),
        ([CelsiusModel(temperature=1.0)], [FahrenheitModel(temperature=33.8)]),
        ([CelsiusModel(temperature=-1.0)], [FahrenheitModel(temperature=30.2)]),
        ([CelsiusModel(temperature=0.1)], [FahrenheitModel(temperature=32.18)]),
        (
            [
                CelsiusModel(temperature=1.0),
                CelsiusModel(temperature=10.0),
                CelsiusModel(temperature=100),
            ],
            [
                FahrenheitModel(temperature=33.8),
                FahrenheitModel(temperature=50.0),
                FahrenheitModel(temperature=212.0),
            ],
        ),
        ([], []),
    ],
    ids=[
        "0",
        "正の数",
        "負の数",
        "少数",
        "複数の値",
        "値を渡さない",
    ],
)
def test_celsius_to_fahrenheit(
    cercius_list: list[CelsiusModel], expected_data: list[FahrenheitModel]
) -> None:
    farhrenheit_list = celsius_to_fahrenheit(cercius_list)
    assert farhrenheit_list == expected_data


@pytest.mark.parametrize(
    "input_number, expected_data",
    [
        (1, list(range(1, 101))),
        (100, [100]),
        (33, [33, 66, 99]),
    ],
    ids=["最小値", "最大値", "サンプル値"],
)
def test_multiple_number(input_number: int, expected_data: list[int]) -> None:
    multiple_list = multiple_number(input_number)
    assert multiple_list == expected_data
