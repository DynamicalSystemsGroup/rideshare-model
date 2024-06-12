## Description

The policy which determines the price of a ride
## Called By
1. [[Request Ride Boundary Action]]
## Domain Spaces
1. [[Request Ride Space]]
## Followed By
## Codomain Spaces
1. [[Request Ride Response Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Ride Pricing Policy $50 Constant, 5 Minutes, Random Driver
#### Description
A dummy policy that always prices the ride at just $50, for 5 minutes waiting time and with a random driver
#### Logic
Update the space to have the ride priced at $50 and 5 minute wait time. Picks a driver randomly from the idle drivers

