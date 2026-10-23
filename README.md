# Виджет банковских операций

## Цель проекта

Проект — бэкенд-часть виджета личного кабинета клиента банка, который показывает последние операции клиента.
Функции проекта маскируют номера карт и счетов, а также фильтруют и сортируют список операций.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/milkabubu/НАЗВАНИЕ_РЕПОЗИТОРИЯ.git
   ```
2. Перейдите в папку проекта:
   ```bash
   cd НАЗВАНИЕ_РЕПОЗИТОРИЯ
   ```
3. Установите зависимости с помощью Poetry:
   ```bash
   poetry install
   ```

## Структура проекта

- `src/masks.py` — функции маскировки номера карты и номера счёта.
- `src/widget.py` — функция маскировки карты или счёта по строке с описанием.
- `src/processing.py` — функции фильтрации и сортировки операций.

## Использование

### Модуль `masks`

`get_mask_card_number` принимает номер карты и возвращает его маску.

```python
from src.masks import get_mask_card_number

get_mask_card_number("7000792289606361")
# '7000 79** **** 6361'
```

`get_mask_account` принимает номер счёта и возвращает его маску.

```python
from src.masks import get_mask_account

get_mask_account("73654108430135874305")
# '**4305'
```

### Модуль `widget`

`mask_account_card` принимает строку с типом и номером карты или счёта и возвращает её с замаскированным номером.

```python
from src.widget import mask_account_card

mask_account_card("Visa Platinum 7000792289606361")
# 'Visa Platinum 7000 79** **** 6361'

mask_account_card("Счет 73654108430135874305")
# 'Счет **4305'
```

### Модуль `processing`

Пример списка операций для функций ниже:

```python
operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
```

#### `filter_by_state`

Принимает список операций и значение для ключа `state` (по умолчанию `"EXECUTED"`).
Возвращает новый список только с теми операциями, у которых `state` совпадает с указанным значением.

```python
from src.processing import filter_by_state

filter_by_state(operations)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

filter_by_state(operations, "CANCELED")
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

#### `sort_by_date`

Принимает список операций и необязательный параметр `reverse`, задающий порядок сортировки:
`True` (по умолчанию) — по убыванию, `False` — по возрастанию.
Возвращает новый список, отсортированный по дате (`date`).

```python
from src.processing import sort_by_date

sort_by_date(operations)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

sort_by_date(operations, reverse=False)
# [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```