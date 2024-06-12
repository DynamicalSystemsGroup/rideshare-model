ride_price_policy_option1 = {
    "name": "Ride Pricing Policy $50 Constant, 5 Minutes, Random Driver",
    "description": "A dummy policy that always prices the ride at just $50, for 5 minutes waiting time and with a random driver",
    "logic": """Update the space to have the ride priced at $50 and 5 minute wait time. Picks a driver randomly from the idle drivers""",
}

ride_pricing_policy = {
    "name": "Ride Pricing Policy",
    "description": "The policy which determines the price of a ride",
    "constraints": [],
    "policy_options": [ride_price_policy_option1],
    "domain": [
        "Request Ride Space",
    ],
    "codomain": [
        "Request Ride Response Space",
    ],
    "parameters_used": [],
    "metrics_used": [],
}

backend_policies = [ride_pricing_policy]
