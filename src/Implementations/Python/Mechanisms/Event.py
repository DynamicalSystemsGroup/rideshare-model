import heapq


def add_event_mechanism(state, params, spaces):
    event = spaces[0]["event"]
    heapq.heappush(
        state["Event Queue"],
        event,
    )
