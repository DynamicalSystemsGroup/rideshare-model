from .Dummy import dummy_policies
from .Backend import backend_policies

policies = []
policies.extend(dummy_policies)
policies.extend(backend_policies)
