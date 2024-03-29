def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return {item: items.count(item) for item in items}


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    for key, value in create_inventory(items).items():
        inventory[key] = inventory.get(key, 0) + value

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for key, value in create_inventory(items).items():
        inventory[key] = inventory.get(key, 0) - value
        inventory[key] = 0 if inventory[key] < 0 else inventory[key]

    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [item for item in inventory.items() if item[1]]

