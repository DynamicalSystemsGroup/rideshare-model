update_driver_state_mechanism = {
    "name": "Update Driver State Mechanism",
    "description": "Mechanism which updates the driver state",
    "constraints": [],
    "logic": "Update the driver from DOMAIN[0] with the state from DOMAIN[0]",
    "domain": ["Driver State Space"],
    "parameters_used": [],
    "updates": [("Driver", "State", False)],
}


driver_mechanisms = [update_driver_state_mechanism]
