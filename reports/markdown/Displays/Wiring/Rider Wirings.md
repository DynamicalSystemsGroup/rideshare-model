## Wiring Diagrams

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

The wirings related to what actions riders take.
## Wirings
1. [[Request Ride Wiring]]

## Unique Components Used
1. [[Add Event Mechanism]]
2. [[Log Ride Request Mechanism]]
3. [[Request Ride Boundary Action]]
4. [[Ride Confirmation Policy]]
5. [[Ride Pricing Policy]]

## Unique Parameters Used

