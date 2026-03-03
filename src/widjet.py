"""Модуль для маскироваки банковских реквизитов доп-функции"""

import re

from masks import get_mask_account, get_mask_card_number


def mask_accout_card(card: str) -> str:
    """Функция для маскировки номера карты:
    Функция mask_account_cardпринимает на вход строку формата
    Visa Platinum 7000792289606361, или Maestro 7000792289606361, или
    Счет 73654108430135874305.
    Для маскировки номера карты/счета используются ранее написанные функции из модуля masks."""
    first_digit_index: int = (re.search(r"\d", card)).start()
    description: str = card[:first_digit_index].strip()
    card_number: str = card[first_digit_index:]
    if description == "Счет":
        masked_info: str = get_mask_account(card_number)
    else:
        masked_info: str = get_mask_card_number(card_number)
    return f"{description} {masked_info}"


def get_date(date: str) -> str:
    """Функция для обработки даты"""
    changed_date: str = date[:10]
    year: str
    month: str
    day: str
    year, month, day = changed_date.split("-", 2)
    return f"{day}.{month}.{year}"
