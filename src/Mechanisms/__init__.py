from .Dummy import dummy_mechanisms
from .Event import event_mechanisms
from .Driver import driver_mechanisms
from .Rider import rider_mechanisms

mechanism = []
mechanism.extend(dummy_mechanisms)
mechanism.extend(event_mechanisms)
mechanism.extend(driver_mechanisms)
mechanism.extend(rider_mechanisms)
