from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Masks a bank card number in the format XXXX XX** **** XXXX.

    Args:
        card_number (Union[int, str]): The original card number.

    Returns:
        str: Masked card number in format 'XXXX XX** **** XXXX'.
    """
    # Преобразуем входные данные в строку без пробелов и других символов
    card_str = str(card_number).replace(" ", "")

    # Проверка длины номера карты (обычно 16 цифр)
    if len(card_str) != 16 or not card_str.isdigit():
        raise ValueError("Card number must be a 16-digit number.")

    # Вырезаем части номера
    first4 = card_str[:4]
    next2 = card_str[4:6]
    middle_block = card_str[6:12]
    last4 = card_str[-4:]

    # Формируем маску по шаблону: XXXX XX** **** XXXX
    masked_card = (
        f"{first4} {next2}** **** {last4}"
    )

    return masked_card


def get_mask_account(account_number: Union[int, str]) -> str:
    """
    Masks a bank account number in the format **XXXX.

    Args:
        account_number (Union[int, str]): The original account number.

    Returns:
        str: Masked account number in format '**XXXX'.
    """
    account_str = str(account_number).replace(" ", "")

    # Проверка длины номера счета (минимум 4 цифры)
    if len(account_str) < 4 or not account_str.isdigit():
        raise ValueError("Account number must be at least 4 digits.")

    last4 = account_str[-4:]

    return f"**{last4}"
