## Description

The boundary action which represents users requesting a ride potentially. Note: There could be a parameter or parameters here that toggle the maximum price that a user is willing to pay (or possibly is randomly selected from a multiple i.e. getting a multiplier picked randomly from [1, 2] that a user is willing to pay versus the non-surge price).
## Called By
1. [[Rider]]

## Followed By
1. [[Ride Pricing Policy]]

## Constraints

## Codomain Spaces
1. [[Request Ride Space]]

## Boundary Action Options:
### 1. Event Queue Request Ride
#### Description
If the top of the event queue is a request ride boundary action then run with that otherwise terminate
#### Logic
Peak at the top of the event queue, if action is for requesting a ride then pop and run the boundary action chain

