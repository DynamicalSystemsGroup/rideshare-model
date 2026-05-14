# Rideshare model — end-to-end pricing-mechanism case study

A canonical example of an end-to-end modeling workflow: ideation → system requirements → mathematical specification → cadCAD implementation → simulation → analysis. The domain is **dynamic pricing and dispatch for a ride-sharing platform**, modeled as a weighted directed graph in which nodes are service regions and edges are travel times between them.

Built using two DSG tools:

- [**MSML**](https://github.com/DynamicalSystemsGroup/MSML) — Mathematical Specification Modeling Language, used to define the formal math spec
- [**cadCAD**](https://github.com/cadCAD-org/cadCAD) — Complex Adaptive Dynamics Computer-Aided Design, used to run the simulation

Maintained by Dynamical Systems Group as a worked example. The repository is structured as a study, not a deployable system.

## Problem framing

The model addresses two coupled questions in ride-share platform design:

1. **Matching**: how should the platform pair available drivers to incoming riders, given a graph of regions with varying demand density and travel-time edges?
2. **Pricing & routing under congestion**: when demand outstrips supply in a region, how should pricing and trip routing respond to keep the system from collapsing into long queues at popular regions?

The work introduces the **Discounted Integral Priority Routing (DIPR)** algorithm — a routing policy that prioritises drivers based on historical queue lengths at candidate regions, with exponential time-discounting so recent congestion weighs heavier than old congestion. DIPR is the central mechanism the simulations evaluate.

## Repository layout

The directories partition the modeling workflow into stages:

| Directory | Stage | Contents |
|---|---|---|
| `research/` | Ideation, definitions, math spec authoring | Curriculum, definitions, MSML scaffold, references, scripts. The `Rideshare/` subfolder contains the worked math spec narrative (Overview, System & Objectives, Variables, Math Spec, Shortest Path). |
| `model/` | MSML model entities | `boundary_actions.py`, `parameters.py`, `spaces.py`, `states.py`, `types.py` — the formal model definitions consumed by MSML |
| `src/` | cadCAD implementation | Implementations of `BoundaryActions/`, `ControlActions/`, `Mechanisms/`, `Metrics/`, `Entities/`, `Parameters/`, `Displays/` — the simulation building blocks |
| `simulation/` | Simulation runtime | `__init__.py`, `config/`, `preprocessing/`, `postprocessing/` — the cadCAD driver setup |
| `experiments/` | Parameter sweeps | `driver_rider/` and `queue/` — specific scenarios run against the model |
| `reports/` | Generated reports | HTML reports produced by MSML's report generator (`Basic Report.html`, dummy-mechanism templates, `markdown/` source) |
| `*.ipynb` | Interactive workflow | `start.ipynb` (entry walkthrough), `implementation.ipynb` (model construction), `Single Simulation.ipynb` (single-run inspection) |

## Workflow

The intended path through the repo:

1. **Read** `research/Rideshare/0 - Overview.md` through `3.1 - Shortest Path.md` — the conceptual setup
2. **Open** `start.ipynb` — walks through the model components in order
3. **Run** `Single Simulation.ipynb` — exercises the cadCAD configuration for a single parameter setting
4. **Inspect** `implementation.ipynb` — the deeper "how was this assembled" view
5. **Generate** reports via MSML's report machinery (see `reports/markdown/`) — produces structured HTML documents that mirror the math spec

## Reproducibility

This repo is a methodology demonstrator and case study, not a library or service. Read it for the workflow; clone it to experiment with parameter sweeps in `experiments/`.

```bash
git clone https://github.com/DynamicalSystemsGroup/rideshare-model.git
cd rideshare-model
# Set up MSML and cadCAD per their respective repos' install instructions
jupyter notebook start.ipynb
```

## Related work at DSG

- [MSML](https://github.com/DynamicalSystemsGroup/MSML) — the mathematical-specification authoring layer
- [gds-core](https://github.com/DynamicalSystemsGroup/gds-core) — the more general dynamical-systems simulation runtime
- [dynamical-block-diagrams](https://github.com/DynamicalSystemsGroup/dynamical-block-diagrams) — formal block-diagram notation for systems like this one
