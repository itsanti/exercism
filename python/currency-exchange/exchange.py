def exchange_money(budget, exchange_rate):
    """
    Return the value of the exchanged currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Return the amount of money that is left from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Return the total value of the given bills.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    Return the number of bills that you can get using the budget.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Return the maximum value of the new currency

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    return get_value_of_bills(denomination, get_number_of_bills(exchange_money(budget, exchange_rate * (1 + spread / 100)), denomination))


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Return the value that is not exchangeable due to the denomination of the bills.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    return int(exchange_money(budget, exchange_rate * (1 + spread / 100))) - exchangeable_value(budget, exchange_rate, spread, denomination)
