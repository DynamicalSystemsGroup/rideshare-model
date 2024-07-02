import heapq


def add_event_mechanism(state, params, spaces):
    event = spaces[0]["event"]
    heapq.heappush(
        state["Event Queue"],
        event,
    )


def log_ride_request_mechanism(state, params, spaces):
    state["Ride Request Log"].append(spaces[0])


def pop_event_mechanism(state, params, spaces):
    heapq.heappop(state["Event Queue"])
