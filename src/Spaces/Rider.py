# This space should have all the attributes necessary to figure out if a [[rider]] who wants a ride ends up getting one.
request_ride_space = {
    "name": "Request Ride Space",
    "schema": {
        "user_id": "User ID Type",
        "source_location": "Geozone Type",
        "target_location": "Geozone Type",
        "maximum_price": "USD Type",
        "maximum_wait_time": "Delta Time Type",
        "ride_time": "Delta Time Type",
        "current_time": "Time Type",
    },
}

# This space builds on the [[Request Ride Space]]. It will have all the same variables as well as the additional variables of:
request_ride_response_space = {
    "name": "Request Ride Response Space",
    "schema": {
        "user_id": "User ID Type",
        "source_location": "Geozone Type",
        "target_location": "Geozone Type",
        "maximum_price": "USD Type",
        "maximum_wait_time": "Delta Time Type",
        "ride_time": "Delta Time Type",
        "current_time": "Time Type",
        "quoted_price": "USD Type",
        "quoted_pickup_time": "Delta Time Type",
        "driver_id": "Driver ID Type",
    },
}

event_space = {
    "name": "Event Space",
    "schema": {"event": "Event Type", "time_added": "Time Type"},
}

rider_state_space = {
    "name": "Rider State Space",
    "schema": {"rider": "User ID Type", "state": "Rider State Type"},
}


rider_spaces = [
    request_ride_space,
    request_ride_response_space,
    event_space,
    rider_state_space,
]
