"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    items_inventory = {}

    for item in items:
        if item in items_inventory:
            prev_value = items_inventory[item]
            items_inventory[item] = prev_value + 1
        else:
            items_inventory.setdefault(item, 1)

    return items_inventory
    


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for item in items:
        if item in inventory:
            prev_value = inventory[item]
            inventory[item] = prev_value + 1
        else:
            inventory.setdefault(item, 1)

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        stock = inventory.get(item, 0)
        if int(stock) <= 0:
            continue
        inventory[item] -= 1

    return inventory

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    availability = inventory.get(item, 0)
    if availability == 0:
        return inventory
    inventory.pop(item)

    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    result = []
    for key in inventory:
        if inventory[key] <= 0:
            continue
        result.append(tuple((key, inventory[key])))

    return result