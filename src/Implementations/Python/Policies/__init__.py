from .Backend import ride_pricing_option1
from .Rider import deterministic_ride_confirmation_policy

policies = {
    "Ride Pricing Policy $50 Constant, 5 Minutes, Random Driver": ride_pricing_option1,
    "Deterministic Ride Confirmation Policy": deterministic_ride_confirmation_policy,
}
