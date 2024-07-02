def create_driver_map(state):
    state["Driver Map"] = {}
    for x in state["Drivers"]:
        state["Driver Map"][x["Driver ID"]] = x
    return state


def create_rider_map(state):
    state["Rider Map"] = {}
    for x in state["Riders"]:
        state["Rider Map"][x["User ID"]] = x
    return state
