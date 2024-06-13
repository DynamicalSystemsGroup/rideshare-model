from .Dummy import dummy_policies
from .Backend import backend_policies
from .Rider import rider_policies

policies = []
policies.extend(dummy_policies)
policies.extend(backend_policies)
policies.extend(rider_policies)
