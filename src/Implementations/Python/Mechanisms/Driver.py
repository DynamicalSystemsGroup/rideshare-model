def update_driver_state_mechanism(state, params, spaces):
    state["Driver Map"][spaces[0]["driver"]]["State"] = spaces[0]["state"]
