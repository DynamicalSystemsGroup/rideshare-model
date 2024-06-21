## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Global")]
EES0(["Event Queue"])
EES0 --- EE0
EES1(["Ride Request Log"])
EES1 --- EE0
end

subgraph X9["Request Ride Wiring"]
direction TB
X1["Request Ride Boundary Action"]
X2["Ride Pricing Policy"]
X3["Ride Confirmation Policy"]
subgraph X8["Request Ride Mechanisms Wiring"]
direction TB
X4["Log Ride Request Mechanism"]
X4 --> EES1
X5["Add Event Mechanism"]
X5 --> EES0
X6[Domain]

direction LR
direction TB
X6 --"Request Ride Response Space"--> X4
X6 --"Event Space"--> X5
end
X1--"Request Ride Space"--->X2
X2--"Request Ride Response Space"--->X3
X3--"Request Ride Response Space
Event Space"---->X8
end
```

## Description

Block Type: Stack Block
The action of a rider requesting a ride.
## Components
1. [[Request Ride Boundary Action]]
2. [[Ride Pricing Policy]]
3. [[Ride Confirmation Policy]]
4. [[Request Ride Mechanisms Wiring]]

## All Blocks
1. [[Add Event Mechanism]]
2. [[Log Ride Request Mechanism]]
3. [[Request Ride Boundary Action]]
4. [[Ride Confirmation Policy]]
5. [[Ride Pricing Policy]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Event Space]]
3. [[Request Ride Response Space]]
4. [[Request Ride Space]]
5. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Event Queue|Event Queue]]
2. [[Global]].[[Global State-Ride Request Log|Ride Request Log]]

