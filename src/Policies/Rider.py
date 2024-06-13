ride_confirmation_policy_option1 = {
    "name": "Deterministic Ride Confirmation Policy",
    "description": "Confirms or rejects the ride as long as all the conditions are met.",
    "logic": """""",
}

ride_confirmation_policy = {
    "name": "Ride Confirmation Policy",
    "description": """This policy will hold the logic of whether or not a [[rider]] confirms the price and time are good with them. There could be policy options to enrich behaviors i.e.

1. Riders only confirm if both the time and price are right for them
2. Riders confirm probabilistically where if both are good it is always true but sometimes they still confirm because they need it badly (but with much lower likelihood)

The [[Request Ride Response Space]] passed in the domain will either come out as the codomain if the user goes with the ride, or it will terminate the process. """,
    "constraints": [],
    "policy_options": [ride_confirmation_policy_option1],
    "domain": [
        "Request Ride Response Space",
    ],
    "codomain": [
        "Request Ride Response Space",
    ],
    "parameters_used": [],
    "metrics_used": [],
}

rider_policies = [ride_confirmation_policy]
