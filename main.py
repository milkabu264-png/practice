from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    test_date = input()
    test_card_or_account = input()
    print(mask_account_card(test_card_or_account))
    print(get_date(test_date))
