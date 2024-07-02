rider_wirings = []

rider_wirings.append(
    {
        "name": "Request Ride Wiring",
        "components": [
            "Request Ride Boundary Action",
            "Ride Pricing Policy",
            "Ride Confirmation Policy",
            "Request Ride Mechanisms Wiring",
        ],
        "description": "The action of a rider requesting a ride.",
        "constraints": [],
        "type": "Stack",
    }
)

rider_wirings.append(
    {
        "name": "Request Ride Mechanisms Wiring",
        "components": [
            "Log Ride Request Mechanism",
            "Add Event Mechanism",
            "Update Driver State Mechanism",
            "Update Rider State Mechanism",
            "Pop Event Mechanism",
        ],
        "description": "Mechanism for ride requests",
        "constraints": [],
        "type": "Parallel",
    }
)
