add_event_mechanism = {
    "name": "Add Event Mechanism",
    "description": "Mechanism which adds an event to the event queue",
    "constraints": [],
    "logic": "Insert the new event into the event queue",
    "domain": [
        "Event Space",
    ],
    "parameters_used": [],
    "updates": [("Global", "Event Queue", False)],
}

pop_event_mechanism = {
    "name": "Pop Event Mechanism",
    "description": "Mechanism which pops the top event from the event queue",
    "constraints": [],
    "logic": "Pop the top event in the event queue",
    "domain": [],
    "parameters_used": [],
    "updates": [("Global", "Event Queue", False)],
}

log_ride_request_mechanism = {
    "name": "Log Ride Request Mechanism",
    "description": "Mechanism which logs rides requested",
    "constraints": [],
    "logic": "Append to the ride request log",
    "domain": ["Request Ride Response Space"],
    "parameters_used": [],
    "updates": [("Global", "Ride Request Log", False)],
}


event_mechanisms = [
    add_event_mechanism,
    log_ride_request_mechanism,
    pop_event_mechanism,
]
