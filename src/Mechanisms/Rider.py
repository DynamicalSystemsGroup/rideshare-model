update_rider_state_mechanism = {
    "name": "Update Rider State Mechanism",
    "description": "Mechanism which updates the rider state",
    "constraints": [],
    "logic": "Update the rider from DOMAIN[0] with the state from DOMAIN[0]",
    "domain": ["Rider State Space"],
    "parameters_used": [],
    "updates": [("Rider", "State", False)],
}


rider_mechanisms = [update_rider_state_mechanism]
