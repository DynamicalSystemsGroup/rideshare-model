from copy import deepcopy
from random import choice


def ride_pricing_option1(state, params, spaces):
    space1 = deepcopy(spaces[0])

    idle_drivers = [x for x in state["Drivers"] if x["State"] == "Idle"]

    if len(idle_drivers) < 0:
        return None

    space1["quoted_price"] = 50
    space1["quoted_pickup_time"] = 5
    space1["driver_id"] = choice(idle_drivers)["Driver ID"]

    return [space1]
