import ru_local as ru


def create_categories() -> dict:
    '''
    function, returning categories of spendings
    :return: categories
    '''
    categories = {
        ru.FOOD: [ru.GORODOK, ru.X5, ru.YARCHE, ru.SAMOKAT, ru.PRODUCTS, ru.DINNER, ru.SUSHI],
        ru.TRANSPORT: [ru.BUS, ru.TAXI, ru.PETROL, ru.SCOOTER],
        ru.AMUSEMENT: [ru.RESTAURANT, ru.THEATRE, ru.CINEMA, ru.CONCERT', ru.TOUR, ru.RECREATION],
        ru.HEALTH: [ru.DOCTOR, ru.DRUGS, ru.HOSPITAL,
                     ru.EYES, ru.DENTIST, ru.PHARMACY],
        ru.HOME: [ru.UTILITIES, ru.RENT, ru.FURNITURE],
        ru.SPORT: [ru.FITNESS, ru.YOGA, ru.POOL, ru.GYM, ru.TENNIS, ru.MASSAGE]
    }
    return categories


def categorize_transaction(description: str, categories: dict) -> str:
    '''
    function returning category for every type of spending in list
    :param: description
    :param: categories
    :return: category of spending or 'другое' if no macthes found
    '''
    description_new = description.lower()
    for category, objects in categories.items():
        for object_ in objects:
            if object_.lower() in description_new:
                return category
    return ru.OTHER


def categorize_all_transactions(transactions: list) -> list:
    '''
    function, returning a list of transactions with added 'category' field
    :param: transactions
    :return: transactions updated
    '''
    categories = create_categories()
    for transaction in transactions:
        description = transaction.get('description', '')
        category_item = categorize_transaction(description, categories)
        transaction.update({'category': category_item})
    return transactions


