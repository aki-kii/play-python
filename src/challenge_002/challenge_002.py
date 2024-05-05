def shout_backwards(string: str) -> str:
    """文字列を逆側から読み、大声で叫ばせるように変換する
    ex: 'DataScienceHub' -> 'BUHECNEICSATAD!!!'

    Args:
        string (str): 変換対象の文字列

    Returns:
        str: 変換後の文字列
    """
    all_caps = string.upper()
    backwards = all_caps[::-1]
    result = backwards + "!!!"
    return result


def squared_primes(array: list[int]) -> list[int]:
    """自然数のリストから素数のみ抜き出して、値を2乗して返す
    ex: [1, 3, 4, 5, 9, 10] -> [9, 25] # (3*3, 5*5)

    Args:
        array (list[int]): 自然数のリスト

    Returns:
        list[int]: 素数の2乗のリスト(素数以外は排除)
    """
    squared_primes = [
        z * z
        for z in [
            x
            for x in array
            if (len([y for y in range(2, x) if x % y == 0]) == 0) & (x > 1)
        ]
    ]
    return squared_primes
