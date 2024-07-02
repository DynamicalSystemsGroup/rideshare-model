from src.Implementations.Python.Utils import Event

state_base = {
    "Riders": [
        {"User ID": 1, "State": "Idle"},
        {"User ID": 2, "State": "Idle"},
        {"User ID": 3, "State": "Idle"},
        {"User ID": 4, "State": "Idle"},
    ],
    "Drivers": [
        {"Driver ID": 1, "State": "Idle"},
        {"Driver ID": 2, "State": "Idle"},
        {"Driver ID": 3, "State": "Idle"},
        {"Driver ID": 4, "State": "Idle"},
    ],
    "Ride Request Log": [],
    "Event Queue": [
        Event(t=5, action="Request Ride", spaces=[{"ride_time": 6}]),
        Event(t=10, action="Request Ride", spaces=[{"ride_time": 50}]),
        Event(t=25, action="Request Ride", spaces=[{"ride_time": 10}]),
    ],
}
