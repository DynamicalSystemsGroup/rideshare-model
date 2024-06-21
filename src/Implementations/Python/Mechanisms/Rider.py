def update_rider_state_mechanism(state, params, spaces):
    state["Rider Map"][spaces[0]["rider"]]["State"] = spaces[0]["state"]
