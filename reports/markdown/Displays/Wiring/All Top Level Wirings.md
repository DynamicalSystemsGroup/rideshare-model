## Wiring Diagrams

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

The wirings which are not components of other wirings.
## Wirings
1. [[Request Ride Wiring]]

## Unique Components Used
1. [[Add Event Mechanism]]
2. [[Log Ride Request Mechanism]]
3. [[Request Ride Boundary Action]]
4. [[Ride Confirmation Policy]]
5. [[Ride Pricing Policy]]
6. [[Update Driver State Mechanism]]
7. [[Update Rider State Mechanism]]

## Unique Parameters Used

