from .Dummy import v1_dummy_boundary, v1_dummy_boundary2, v2_dummy_boundary2
from .User import event_queue_request_ride

boundary_action_options = {
    "V1 Dummy Boundary Action Option": v1_dummy_boundary,
    "V1 Dummy Boundary Action 2 Option": v1_dummy_boundary2,
    "V2 Dummy Boundary Action 2 Option": v2_dummy_boundary2,
    "Event Queue Request Ride": event_queue_request_ride,
}
