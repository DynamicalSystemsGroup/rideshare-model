ride_confirmation_policy_option1 = {
    "name": "Deterministic Ride Confirmation Policy",
    "description": "Confirms or rejects the ride as long as all the conditions are met.",
    "logic": """Pass on the space as long as domain[0]["quoted_price"] <= domain[0]["maximum_price"] and domain[0]["quoted_pickup_time"] <= domain[0]["maximum_wait_time"]""",
}


def deterministic_ride_confirmation_policy(state, params, spaces):
    domain = spaces
    if (
        domain[0]["quoted_price"] <= domain[0]["maximum_price"]
        and domain[0]["quoted_pickup_time"] <= domain[0]["maximum_wait_time"]
    ):
        return spaces
    else:
        return None
