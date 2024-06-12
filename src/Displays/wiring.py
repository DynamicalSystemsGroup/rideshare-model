wiring_display = []
wiring_display.append(
    {
        "name": "All Top Level Wirings",
        "description": "The wirings which are not components of other wirings.",
        "components": [
            "Dummy Boundary Wiring",
            "Dummy Boundary Wiring 2",
            "Dummy Control Wiring",
            "Request Ride Wiring",
        ],
    }
)
wiring_display.append(
    {
        "name": "Boundary Action Wirings",
        "description": "The wirings related to only boundary type actions.",
        "components": [
            "Dummy Boundary Wiring",
            "Dummy Boundary Wiring 2",
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
