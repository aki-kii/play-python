from typing import Any

import pytest

from challenge_002.challenge_002 import shout_backwards, squared_primes


@pytest.mark.parametrize(
    "input_text, expected_text",
    [
        ("text", "TXET!!!"),
        ("TEXT", "TXET!!!"),
        ("てきすと", "とすきて!!!"),
        ("a", "A!!!"),
        ("", "!!!"),
    ],
    ids=[
        "大文字に変換できる文字列",
        "大文字に変換されている文字列",
        "大文字に変換できない文字列",
        "1文字の文字列",
        "空文字",
    ],
)
def test_shout_backwards(input_text: str, expected_text: str) -> None:
    shout_text = shout_backwards(input_text)
    assert shout_text == expected_text


@pytest.mark.parametrize(
    "input_numbers, expected_numbers",
    [
        ([2, 3, 5], [4, 9, 25]),
        ([1, 2, 3], [4, 9]),
        ([1, 4, 9], []),
        ([-1, 1, 2], [4]),
        ([2, 3, 92693], [4, 9, 8591992249]),
        ([3, 2, 5], [9, 4, 25]),
        ([2], [4]),
        ([], []),
    ],
    ids=[
        "素数のみ",
        "素数と素数以外が混合",
        "素数以外のみ",
        "負の数が混合",
        "巨大な数が混合",
        "ソートされていない",
        "リストが1つの値",
        "リストが空",
    ],
)
def test_squared_primes(input_numbers: list[int], expected_numbers: list[int]) -> None:
    results = squared_primes([2, 3, 5])
    assert results == [4, 9, 25]
