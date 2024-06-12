request_ride_boundary_action_option1 = {
    "name": "Event Queue Request Ride",
    "description": "If the top of the event queue is a request ride boundary action then run with that otherwise terminate",
    "logic": "Peak at the top of the event queue, if action is for requesting a ride then pop and run the boundary action chain",
}


request_ride_boundary_action = {
    "name": "Request Ride Boundary Action",
    "description": "The boundary action which represents users requesting a ride potentially. Note: There could be a parameter or parameters here that toggle the maximum price that a user is willing to pay (or possibly is randomly selected from a multiple i.e. getting a multiplier picked randomly from [1, 2] that a user is willing to pay versus the non-surge price).",
    "constraints": [],
    "boundary_action_options": [request_ride_boundary_action_option1],
    "called_by": ["Rider"],
    "codomain": [
        "Request Ride Space",
    ],
    "parameters_used": [],
}
