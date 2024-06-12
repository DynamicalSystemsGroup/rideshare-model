from random import choice


def event_queue_request_ride(state, params, spaces):

    # Only trigger if the event queue action is request ride
    if state["Event Queue"][0].action != "Request Ride":
        return

    t = state["Event Queue"][0].t
    spaces = state["Event Queue"][0].spaces

    idle_riders = [x for x in state["Riders"] if x["State"] == "Idle"]

    if len(idle_riders) < 0:
        return None

    # Random assumptions for now
    space = {
        "user_id": choice(idle_riders)["User ID"],
        "source_location": "TBD",
        "target_location": "TBD",
        "maximum_price": 100,
        "maximum_wait_time": 5,
        "ride_time": spaces[0]["ride_time"],
        "current_time": t,
    }
    return [space]
