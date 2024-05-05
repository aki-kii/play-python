from challenge_001.celsius_model import CelsiusModel
from challenge_001.fahrenheit_model import FahrenheitModel


def celsius_to_fahrenheit(celsius_list: list[CelsiusModel]) -> list[FahrenheitModel]:
    """Celsius温度のリストをFahrenheit温度のリストに変換する

    Args:
        celsius_list (list[CelsiusModel]): Celsius温度のリスト

    Returns:
        list[FahrenheitModel]: Fahrenheit温度のリスト
    """
    return [
        FahrenheitModel(temperature=celsius.to_fahrenheit()) for celsius in celsius_list
    ]


def multiple_number(input_number: int) -> list[int]:
    """100以下の自然数を指定すると倍数の一覧をリストで返す

    Args:
        input_number (int): 入力された100以下の自然数

    Returns:
        list[int]: 入力された数の倍数が全て含まれるリスト
    """
    # 100以下の倍数の個数
    multiple_size = 100 // input_number

    return [i * input_number for i in range(1, multiple_size + 1)]
