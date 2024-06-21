def deterministic_ride_confirmation_policy(state, params, spaces):
    domain = spaces
    if (
        domain[0]["quoted_price"] <= domain[0]["maximum_price"]
        and domain[0]["quoted_pickup_time"] <= domain[0]["maximum_wait_time"]
    ):
        return spaces
    else:
        return None
