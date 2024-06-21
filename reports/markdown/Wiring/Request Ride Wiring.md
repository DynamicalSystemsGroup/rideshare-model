## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Driver")]
EE1[("Global")]
EE2[("Rider")]
EES0(["State"])
EES0 --- EE0
EES1(["Event Queue"])
EES1 --- EE1
EES2(["Ride Request Log"])
EES2 --- EE1
EES3(["State"])
EES3 --- EE2
end

subgraph X11["Request Ride Wiring"]
direction TB
X1["Request Ride Boundary Action"]
X2["Ride Pricing Policy"]
X3["Ride Confirmation Policy"]
subgraph X10["Request Ride Mechanisms Wiring"]
direction TB
X4["Log Ride Request Mechanism"]
X4 --> EES2
X5["Add Event Mechanism"]
X5 --> EES1
X6["Update Driver State Mechanism"]
X6 --> EES0
X7["Update Rider State Mechanism"]
X7 --> EES3
X8[Domain]

direction LR
direction TB
X8 --"Request Ride Response Space"--> X4
X8 --"Event Space"--> X5
X8 --"Driver State Space"--> X6
X8 --"Rider State Space"--> X7
end
X1--"Request Ride Space"--->X2
X2--"Request Ride Response Space"--->X3
X3--"Request Ride Response Space
Event Space
Driver State Space
Rider State Space"------>X10
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
6. [[Update Driver State Mechanism]]
7. [[Update Rider State Mechanism]]

## Constraints

## Domain Spaces

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Driver State Space]]
2. [[Empty Space]]
3. [[Event Space]]
4. [[Request Ride Response Space]]
5. [[Request Ride Space]]
6. [[Rider State Space]]
7. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Driver]].[[Driver State-State|State]]
2. [[Global]].[[Global State-Event Queue|Event Queue]]
3. [[Global]].[[Global State-Ride Request Log|Ride Request Log]]
4. [[Rider]].[[Rider State-State|State]]

