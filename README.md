# ⛏️ Mining Process Optimization with Multi-Objective Genetic Algorithm

This Python project uses a **Multi-Objective Genetic Algorithm (MOGA)** to optimize a sequence of mining processes. The algorithm evaluates trade-offs between economic return, worker benefit, total duration, and adoption of Industry 4.0 components. Created for self-learning purposes, it does not reflect reality, much less the application in a specialized process based on datasets. It only seeks to integrate a concept into the work of this specific algorithm design (it was one of the first Python codes I made.)

---

## 🎯 Objectives

- 🧠 **Model mining processes** with attributes like duration, economic return, and associated Industry 4.0 technologies.
- 🤖 **Apply a genetic algorithm** to optimize multi-objective trade-offs.
- ⚙️ Simulate real-world sequencing decisions under **technological constraints** (e.g., continuity in automation).
- 🧬 Identify **non-dominated solutions** using Pareto efficiency logic.

---

## 📦 Features

- **15 mining processes** modeled with durations, economic values, and 4.0-related technologies.
- **Custom evaluation function** considering:
  - Economic performance
  - Worker benefit
  - Process duration
  - Presence of Industry 4.0 components
- **Penalty system** for broken automation chains
- **Multi-objective selection** based on non-dominated sorting
- **Elitism** for preserving top-performing solutions
- **Random crossover and mutation**
- **Dominance validation logic** to ensure solution quality

---

## 🧮 Fitness Function

Each chromosome is evaluated on:

1. 💰 `economic_performance = sum(duration × value)`
2. 👷 `worker_benefit = sum(value)`
3. ⏱️ `total_duration = sum(duration)`
4. ⚙️ `4.0_components = union of all components in selected processes`

If a process with `"Automation and intelligent control"` follows one **without it**, economic performance is penalized by 50%.

---

## 📊 Output Example (per generation)

```text
Generation: 35
Best chromosome: [1, 13, 6, 4, 12, ...]
Economic Performance: 30400
Worker Benefit: 980
Total Duration: 72
4.0 Components Present: ['Automation and intelligent control', 'Big Data', 'Cybersecurity']
Fitness: (30400, 980, 72)
```


## 🚀 How to Run
```bash
python3 mining_moga.py
```

---


##📘 Suggested Educational Uses

Course: Industrial Optimization / Smart Mining

Topics:

- Genetic algorithms

- Multi-objective optimization

- Process sequencing

- Industry 4.0 adoption

Activities:

- Adjust mutation rate, elitism, or penalty rules

- Add new processes or technologies

- Visualize trade-offs in solution space

---


## 🔍 Notes

- Algorithm is non-deterministic: different runs will yield different Pareto fronts.

- Includes dominance-checking logic to avoid selecting dominated solutions.

- Designed for interpretability and teaching, not high-performance computing.

---


##🧑‍💻 Author

Gustavo Alcántara
