from ..Utils import Event


def deterministic_ride_confirmation_policy(state, params, spaces):
    domain = spaces
    if (
        domain[0]["quoted_price"] <= domain[0]["maximum_price"]
        and domain[0]["quoted_pickup_time"] <= domain[0]["maximum_wait_time"]
    ):

        event = Event(
            t=domain[0]["current_time"]
            + domain[0]["ride_time"]
            + domain[0]["quoted_pickup_time"],
            action="Complete Ride",
            spaces=[{}],
        )
        event_space = {"event": event, "time_added": domain[0]["current_time"]}
        space3 = {"driver": domain[0]["driver_id"], "state": "En Route"}
        space4 = {"rider": domain[0]["user_id"], "state": "En Route"}
        return [domain[0], event_space, space3, space4]
    else:
        return None
