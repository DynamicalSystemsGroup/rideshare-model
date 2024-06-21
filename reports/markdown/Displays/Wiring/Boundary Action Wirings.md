## Wiring Diagrams

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Variable A"])
EES0 --- EE0
end

subgraph X4["Dummy Boundary Wiring"]
direction TB
X1["Dummy Boundary Action"]
X2["Dummy Policy"]
X3["Dummy Mechanism"]
X3 --> EES0
X1--"Dummy Space 1"--->X2
X2--"Dummy Space 2"--->X3
end
```

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Variable A"])
EES0 --- EE0
end

subgraph X4["Dummy Boundary Wiring 2"]
direction TB
X1["Dummy Boundary Action 2"]
X2["Dummy Policy"]
X3["Dummy Mechanism"]
X3 --> EES0
X1--"Dummy Space 1"--->X2
X2--"Dummy Space 2"--->X3
end
```

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

The wirings related to only boundary type actions.
## Wirings
1. [[Dummy Boundary Wiring]]
2. [[Dummy Boundary Wiring 2]]
3. [[Request Ride Wiring]]

## Unique Components Used
1. [[Add Event Mechanism]]
2. [[Dummy Boundary Action]]
3. [[Dummy Boundary Action 2]]
4. [[Dummy Mechanism]]
5. [[Dummy Policy]]
6. [[Log Ride Request Mechanism]]
7. [[Request Ride Boundary Action]]
8. [[Ride Confirmation Policy]]
9. [[Ride Pricing Policy]]

## Unique Parameters Used
1. [[dummy_parameter]]

