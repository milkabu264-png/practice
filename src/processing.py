"""
Модуль для отображения последних операций пользователя.
"""


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция для фильтрации операций по статусу.
    Функция filter_by_state принимает на вход список словарей с операциями
    и значение для ключа state (по умолчанию EXECUTED).
    Возвращает новый список, в котором остались только операции с указанным статусом."""
    selected_operations: list[dict] = []
    for operation in operations:
        if operation.get("state") == state:
            selected_operations.append(operation)
    return selected_operations


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция для сортировки операций по дате.
    Функция sort_by_date принимает на вход список словарей с операциями
    и необязательный параметр reverse, задающий порядок сортировки
    (по умолчанию True — по убыванию, False — по возрастанию).
    Возвращает новый список, отсортированный по ключу date."""
    return sorted(operations, key=lambda operation: operation["date"], reverse=reverse)
