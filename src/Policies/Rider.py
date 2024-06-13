ride_confirmation_policy_option1 = {
    "name": "Deterministic Ride Confirmation Policy",
    "description": "Confirms or rejects the ride as long as all the conditions are met.",
    "logic": """""",
}

ride_confirmation_policy = {
    "name": "Ride Confirmation Policy",
    "description": "The policy which determines the price of a ride",
    "constraints": [],
    "policy_options": [ride_confirmation_policy_option1],
    "domain": [
        "Request Ride Space",
    ],
    "codomain": [
        "Request Ride Response Space",
    ],
    "parameters_used": [],
    "metrics_used": [],
}

rider_policies = [ride_confirmation_policy]
