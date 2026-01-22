# ✈️ Flight Route Planner & Evaluation

Implementation and evaluation of AI search algorithms applied to the task of a flight route planner. This project compares Breadth-First Search (BFS), Depth-First Search (DFS), Best-First Search, and A* Search algorithms in finding optimal flight routes.

The comprehensive report, including features implemented, design decisions, evaluation results, and testing can be found in the [report](./report/) directory.

---

## 👥 Project Team

| Name | Role | Contact |
|------|------|---------|
| **Ankit Kumar Karn**
| **Kshitiz Khanal** 
| **Royas Shakya**
| **Aditya Shrestha**

---

## 🎯 Project Overview

### 🚫 Constraints
- The **pole state (0,0)** is forbidden.
- User-defined **obstacles** block specific locations.

### 🔍 Search Algorithms Included
| Algorithm | Type | Optimal | Notes |
|----------|------|---------|------|
| BFS | Uninformed | ✅ Yes (shortest steps) | Expands many nodes |
| DFS | Uninformed | ❌ No | Can produce long paths |
| Best-First | Informed | ❌ No | Greedy heuristic based |
| A* Search | Informed | ✅ Yes (lowest cost) | Uses cost + heuristic |

### 📊 Evaluation Metrics
The algorithms are compared using:
- **Path length**
- **Path cost**
- **Nodes expanded**
- **Node depth**
- **Nodes created**
- **Runtime (ms)**

## Installation

1. Clone the project: `https://github.com/shkroyas/Flight-Route-Planner`

2. Cd into the directory and compile the files:

```
cd Flight-Route-Planner
javac src/A1Main.java
```

## Usage

`java A1Main <search_type> <world_size> <start_goal> <end_goal> [<obstacles>]`

where:
* `search_type` is the type of search algorithm to use to find a solution e.g. DFS, BFS, AStar, BestF.
* `world_size` is the size of the world *N* (number of parallels).
* `start_goal` is the starting point of the agent.
* `end_goal` is the goal point that the agent must reach.
* `obstacles` is a number of points that the search algorithms cannot take when looking for a route.
    
Examples:

* BFS: `java A1Main BFS 5 2,45 3,225`
* DFS: `java A1Main DFS 8 1,315 5,270`
* BestF with 1 obstacle: `java A1Main BestF 4 1,45 3,225 1,90`
* A* with 2 obstacles: `java A1Main AStar 4 1,45 3,225 1,90 1,0`
* No route: `java A1Main BFS 4 1,45 3,225 1,90 1,0 2,45`
