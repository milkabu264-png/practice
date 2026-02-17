"""
Модуль для маскировки банковских реквизитов.
"""

import re


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая преобразует номер карты в маску"""
    space_index: int = card_number.find(' ')
    card_mask: str = ""
    if not re.fullmatch(r"\d{16}", card_number):
        raise ValueError(f"Номер карты {card_number} не валиден." "Ожидается 16 цифр. ")
    card_mask = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return card_mask


def get_mask_account(account_number: str) -> str:
    """Функция, которая преобразует номер счета в маску"""

    clean_account: str = account_number.replace(" ", "")

    # Проверяем, что это цифры и длина >= 4
    if not clean_account.isdigit() or len(clean_account) < 4:
        raise ValueError(f"Номер счета {account_number} не валиден. Ожидаются цифры (минимум 4).")

    return f"**{clean_account[-4:]}"
