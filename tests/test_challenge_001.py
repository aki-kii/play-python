import pytest

from challenge_001 import multiple_number, to_fahrenheit


@pytest.mark.parametrize(
    "cercius_list, expected_data",
    [
        pytest.param([0.0], [32.0], id="zero"),
        pytest.param([1.0], [33.8], id="natural number"),
        pytest.param([-1.0], [30.2], id="negative number"),
        pytest.param([0.1], [32.18], id="decimal number"),
        pytest.param([1.0, 10.0, 100], [33.8, 50.0, 212.0], id="multiple number"),
        pytest.param([], [], id="empty number"),
    ],
)
def test_to_fahrenheit(cercius_list, expected_data):
    farhrenheit_list = to_fahrenheit(cercius_list)
    assert farhrenheit_list == expected_data


@pytest.mark.parametrize(
    "input_number, expected_data",
    [
        pytest.param(1, list(range(1, 101)), id="minimum number"),
        pytest.param(100, [100], id="maximum number"),
        pytest.param(33, [33, 66, 99], id="sampling number"),
    ],
)
def test_multiple_number(input_number, expected_data):
    multiple_list = multiple_number(input_number)
    assert multiple_list == expected_data
