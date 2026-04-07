# consts
USD_TO_RUB = 78.68


def convert_usd_to_rub(usd: float) -> float:
    """
    Конвертация долларов (USD) в рубли (РУБ)

    :param usd: float
    :return: float
    """

    return usd * USD_TO_RUB


amount_usd = float(input('Введите сумму в долларах (USD): '))
amount_rub = convert_usd_to_rub(amount_usd)
print(f'{amount_usd:.2f} USD -> {amount_rub:.2f} РУБ  (по указанному курсу)')
