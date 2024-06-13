## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
end

subgraph X4["Request Ride Wiring"]
direction TB
X1["Request Ride Boundary Action"]
X2["Ride Pricing Policy"]
X3["Ride Confirmation Policy"]
X1--"Request Ride Space"--->X2
X2--"Request Ride Response Space"--->X3
end
```

## Description

Block Type: Stack Block
The action of a rider requesting a ride.
## Components
1. [[Request Ride Boundary Action]]
2. [[Ride Pricing Policy]]
3. [[Ride Confirmation Policy]]

## All Blocks
1. [[Request Ride Boundary Action]]
2. [[Ride Confirmation Policy]]
3. [[Ride Pricing Policy]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Request Ride Response Space]]

## All Spaces Used
1. [[Request Ride Response Space]]
2. [[Request Ride Space]]

## Parameters Used

## Called By

## Calls

## All State Updates

