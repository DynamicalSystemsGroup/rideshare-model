wiring_display = []
wiring_display.append(
    {
        "name": "All Top Level Wirings",
        "description": "The wirings which are not components of other wirings.",
        "components": [
                                                "Request Ride Wiring",
        ],
    }
)
wiring_display.append(
    {
        "name": "Boundary Action Wirings",
        "description": "The wirings related to only boundary type actions.",
        "components": [
                                    "Request Ride Wiring",
        ],
    }
)

wiring_display.append(
    {
        "name": "Rider Wirings",
        "description": "The wirings related to what actions riders take.",
        "components": [
            "Request Ride Wiring",
        ],
    }
)
