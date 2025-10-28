def create_categories() -> dict:
    categories = {
        'еда': ['городок', 'пятёрочка', 'ярче', 'самокат', 'продукты', 'обед', 'суши'],
        'транспорт': ['автобус', 'такси', 'бензин', 'самокат'],
        'развлечения': ['ресторан', 'театр', 'кино', 'концерт', 'тур', 'отдых'],
        'здоровье': ['врач', 'лекарства', 'больница',
                     'глаза', 'стоматолог', 'аптека'],
        'дом': ['коммунальные услуги', 'аренда квартиры', 'мебель'],
        'спорт': ['фитнес', 'йога', 'бассейн', 'зал', 'теннис', 'массаж']
    }
    return categories


def categorize_transaction(description: str, categories: dict) -> str:
    description_new = description.lower()
    for category, objects in categories.items():
        for object_ in objects:
            if object_.lower() in description_new:
                return category
    return 'другое'


def categorize_all_transactions(transactions: list) -> list:
    categories = create_categories()
    for transaction in transactions:
        description = transaction.get("description", "")
        category_item = categorize_transaction(description, categories)
        transaction.update({"category": category_item})
    return transactions
