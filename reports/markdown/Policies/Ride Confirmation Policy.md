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
## Codomain Spaces
1. [[Request Ride Response Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Deterministic Ride Confirmation Policy
#### Description
Confirms or rejects the ride as long as all the conditions are met.
#### Logic


