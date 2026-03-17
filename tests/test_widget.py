import pytest
from widget import mask_account_card, get_date

@pytest.mark.parametrize(
    "input_data, expected_type",
    [
        ("4111 1111 1111 1111", "card"),
        ("6176543210", "account"),
        ("invalid", "unknown"),
        ("", "unknown"),
        (None, "unknown"),
    ]
)
def test_mask_account_card(input_data, expected_type):
    result = mask_account_card(input_data)
    assert isinstance(result, str)
    # Можно добавить проверки содержания результата в зависимости от типа

@pytest.mark.parametrize(
    "input_date, expected_date",
    [
        ("2023-09-01", "01.09.2023"),
        ("01/09/2023", "01.09.2023"),
        ("2023/09/01", "01.09.2023"),
        ("", ""),
        (None, ""),
    ]
)
def test_get_date(input_date, expected_date):
    result = get_date(input_date)
    assert result == expected_date