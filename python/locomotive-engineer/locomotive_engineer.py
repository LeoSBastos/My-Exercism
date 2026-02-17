"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*input_data):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(input_data)


def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    error_wagons = each_wagons_id[0:2]
    each_wagons_id = each_wagons_id[3:]
    new_wagons_list = [1]
    new_wagons_list.extend(missing_wagons)
    new_wagons_list.extend(each_wagons_id)
    new_wagons_list.extend(error_wagons)
    return new_wagons_list


def add_missing_stops(route: dict, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route['stops'] = list(stops.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return list(map(list, zip(*wagons_rows)))
