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

event_mechanisms = [add_event_mechanism]
