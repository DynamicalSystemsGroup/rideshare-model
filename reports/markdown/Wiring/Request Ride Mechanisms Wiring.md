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

subgraph X8["Request Ride Mechanisms Wiring"]
direction TB
X1["Log Ride Request Mechanism"]
X1 --> EES2
X2["Add Event Mechanism"]
X2 --> EES1
X3["Update Driver State Mechanism"]
X3 --> EES0
X4["Update Rider State Mechanism"]
X4 --> EES3
X5["Pop Event Mechanism"]
X5 --> EES1
X6[Domain]

direction LR
direction TB
X6 --"Request Ride Response Space"--> X1
X6 --"Event Space"--> X2
X6 --"Driver State Space"--> X3
X6 --"Rider State Space"--> X4
X6 --> X5
end
```

## Description

Block Type: Parallel Block
Mechanism for ride requests
## Components
1. [[Log Ride Request Mechanism]]
2. [[Add Event Mechanism]]
3. [[Update Driver State Mechanism]]
4. [[Update Rider State Mechanism]]
5. [[Pop Event Mechanism]]

## All Blocks
1. [[Add Event Mechanism]]
2. [[Log Ride Request Mechanism]]
3. [[Pop Event Mechanism]]
4. [[Update Driver State Mechanism]]
5. [[Update Rider State Mechanism]]

## Constraints

## Domain Spaces
1. [[Request Ride Response Space]]
2. [[Event Space]]
3. [[Driver State Space]]
4. [[Rider State Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Driver State Space]]
2. [[Empty Space]]
3. [[Event Space]]
4. [[Request Ride Response Space]]
5. [[Rider State Space]]
6. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Driver]].[[Driver State-State|State]]
2. [[Global]].[[Global State-Event Queue|Event Queue]]
3. [[Global]].[[Global State-Ride Request Log|Ride Request Log]]
4. [[Rider]].[[Rider State-State|State]]

