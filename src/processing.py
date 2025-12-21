def filter_by_state(records, state='EXECUTED'):
    """
    Возвращает новый список словарей, где значение ключа 'state' совпадает с переданным.

    :param records: список словарей с операциями
    :param state: значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED')
    :return: список словарей с нужным состоянием
    """
    return [record for record in records if record.get('state') == state]


def sort_by_date(records, reverse=True):
    """
    Возвращает новый отсортированный список по дате.

    :param records: список словарей с операциями
    :param reverse: если True, сортировка по убыванию (по умолчанию)
    :return: отсортированный список словарей
    """
    return sorted(records, key=lambda x: x.get('date', ''), reverse=reverse)