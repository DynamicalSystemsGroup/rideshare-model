from src.Implementations.Python.Utils import Event

experiments_map = {}

test_blocks = ["Request Ride Wiring", "Request Ride Wiring"]


experiments_map["Simple Test"] = {
    "Name": "Baseline",
    "Param Modifications": None,
    "State Modifications": {
        "Event Queue": [
            Event(t=5, action="Request Ride", spaces=[{"ride_time": 6}]),
            Event(t=10, action="Request Ride", spaces=[{"ride_time": 50}]),
        ]
    },
    "Blocks": test_blocks,
    "Monte Carlo Runs": 5,
}
