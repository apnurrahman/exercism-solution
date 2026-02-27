"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    
    moved_wagons_1, moved_wagons_2, index, *remaining = each_wagons_id
    moved = list((moved_wagons_1, moved_wagons_2))
    prefix = [index] + missing_wagons
    *fixed_wagons, = *prefix, *remaining, *moved
    
    return fixed_wagons

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    
    city_stops = []
    for value in kwargs.values():
        city_stops.append(value)
    route.setdefault("stops", city_stops)

    return route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    
    #combining two dicts
    extended_route_information =  {**route, **more_route_information}

    return extended_route_information    


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    first_row, second_row, third_row = wagons_rows
    result = []
    #we're gonna repack those three into a list of tuples. No * (asterisk) is involved in packing.
    for tuple in zip(first_row, second_row, third_row):
        result.append(list(tuple))

    return result