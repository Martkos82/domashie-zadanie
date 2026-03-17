import pytest
from masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize(
    "input_number, expected_mask",
    [
        ("1234567812345678", "**** **** **** 5678"),
        ("987654321", "***** 4321"),
        ("", ""),           # пустая строка
        (None, ""),        # None (если функция умеет так обрабатывать)
        ("1234", "1234"),  # меньшая длина
    ]
)
def test_get_mask_card_number(input_number, expected_mask):
    result = get_mask_card_number(input_number)
    assert result == expected_mask

@pytest.mark.parametrize(
    "input_account, expected_mask",
    [
        ("1234567890", "******7890"),
        ("98765", "*****"),
        ("", ""),
        (None, ""),
        ("123", "123"),
    ]
)
def test_get_mask_account(input_account, expected_mask):
    result = get_mask_account(input_account)
    assert result == expected_mask