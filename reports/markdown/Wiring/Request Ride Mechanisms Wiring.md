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

subgraph X5["Request Ride Mechanisms Wiring"]
direction TB
X1["Log Ride Request Mechanism"]
X1 --> EES1
X2["Add Event Mechanism"]
X2 --> EES0
X3[Domain]

direction LR
direction TB
X3 --"Request Ride Response Space"--> X1
X3 --"Event Space"--> X2
end
```

## Description

Block Type: Parallel Block
Mechanism for ride requests
## Components
1. [[Log Ride Request Mechanism]]
2. [[Add Event Mechanism]]

## All Blocks
1. [[Add Event Mechanism]]
2. [[Log Ride Request Mechanism]]

## Constraints

## Domain Spaces
1. [[Request Ride Response Space]]
2. [[Event Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Event Space]]
3. [[Request Ride Response Space]]
4. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Global]].[[Global State-Event Queue|Event Queue]]
2. [[Global]].[[Global State-Ride Request Log|Ride Request Log]]

