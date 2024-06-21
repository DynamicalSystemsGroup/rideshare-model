## Description

This policy will hold the logic of whether or not a [[rider]] confirms the price and time are good with them. There could be policy options to enrich behaviors i.e.

1. Riders only confirm if both the time and price are right for them
2. Riders confirm probabilistically where if both are good it is always true but sometimes they still confirm because they need it badly (but with much lower likelihood)

The [[Request Ride Response Space]] passed in the domain will either come out as the codomain if the user goes with the ride, or it will terminate the process. 
## Called By
1. [[Ride Pricing Policy]]
## Domain Spaces
1. [[Request Ride Response Space]]
## Followed By
1. [[Log Ride Request Mechanism]]
2. [[Add Event Mechanism]]
3. [[Update Driver State Mechanism]]
4. [[Update Rider State Mechanism]]
## Codomain Spaces
1. [[Request Ride Response Space]]
2. [[Event Space]]
3. [[Driver State Space]]
4. [[Rider State Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Deterministic Ride Confirmation Policy
#### Description
Confirms or rejects the ride as long as all the conditions are met.
#### Logic
Pass on the space as long as domain[0]["quoted_price"] <= domain[0]["maximum_price"] and domain[0]["quoted_pickup_time"] <= domain[0]["maximum_wait_time"]

