import heapq


# Function to initialize the event queue with a list of initial events, can add any # of events here
def initialize_event_queue(state) -> dict:
    initial_events = state["Event Queue"]
    heapq.heapify(initial_events)
    return state
