
from masks import get_mask_account, get_mask_card_number

def mask_accout_card(card: str) -> str:
    """Функция для маскировки номера карты:
      Функция mask_account_cardпринимает на вход строку формата
      Visa Platinum 7000792289606361, или Maestro 7000792289606361, или
      Счет 73654108430135874305.
      Для маскировки номера карты/счета используются ранее написанные функции из модуля masks."""
    description, card_number = card.split(' ', 1)
    if description == "Счет":
        return get_mask_account(card_number)
    else:
        return get_mask_card_number(card_number)
def get_date(date: str) -> str:
    changed_date: str = date[:9]
    day, month, year = changed_date.split('-', 2)
    return(f"{day}.{month}.{year}")

