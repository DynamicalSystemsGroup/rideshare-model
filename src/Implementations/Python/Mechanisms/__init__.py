from .Event import add_event_mechanism, log_ride_request_mechanism, pop_event_mechanism
from .Driver import update_driver_state_mechanism
from .Rider import update_rider_state_mechanism

mechanisms = {
    "Add Event Mechanism": add_event_mechanism,
    "Log Ride Request Mechanism": log_ride_request_mechanism,
    "Update Driver State Mechanism": update_driver_state_mechanism,
    "Update Rider State Mechanism": update_rider_state_mechanism,
    "Pop Event Mechanism": pop_event_mechanism,
}
