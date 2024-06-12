## Wiring Diagrams

```mermaid
graph TB

subgraph SVS["State Variables"]
end

subgraph X3["Request Ride Wiring"]
direction TB
X1["Request Ride Boundary Action"]
X2["Ride Pricing Policy"]
X1--"Request Ride Space"--->X2
end
```

## Description

The wirings related to what actions riders take.
## Wirings
1. [[Request Ride Wiring]]

## Unique Components Used
1. [[Request Ride Boundary Action]]
2. [[Ride Pricing Policy]]

## Unique Parameters Used

