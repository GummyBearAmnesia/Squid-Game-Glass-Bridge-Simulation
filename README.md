# Glass Bridge Survival Simulation 🎲

This project simulates the probability of contestants successfully crossing a **bridge of 18 platforms**, where each step has a 50/50 chance of survival (safe vs. falling). The simulation runs many trials to estimate each contestant’s chances of survival depending on their position in line.

---

## 🔹 Project Overview

* **Trial()**:
  Simulates one run of the game for 16 contestants.

  * Each contestant moves forward platform by platform.
  * At each platform, they have a 50% chance of falling (fate = 0) or surviving (fate = 1).
  * If a contestant falls, the next contestant benefits from knowing which platforms were safe up to that point.
  * The bridge has **18 platforms maximum**, and if a contestant reaches that, they’re considered to have crossed successfully.

* **Simulation()**:
  Runs **10,000 trials** of the game.

  * Tracks how many times each contestant reaches the end.
  * Calculates the probability of survival for each contestant.
  * Prints both raw success counts and probabilities.

---

## 🔹 Key Logic

* Contestant **1** has no knowledge and must guess from the start.
* Contestant **N > 1** starts with knowledge of where contestant **N-1** fell, giving them a slightly higher chance of survival.
* Over many trials, contestants who go **later** generally have a **higher chance** of crossing.

---

## 🔹 Example Output

```
SUCCESSES:
{1: 7, 2: 13, 3: 34, 4: 87, 5: 175, ..., 16: 9825}

PROBABILITIES:
{1: 0.0007, 2: 0.0013, 3: 0.0034, 4: 0.0087, 5: 0.0175, ..., 16: 0.9825}
```

Interpretation:

* Contestant 1 almost never makes it across.
* Contestant 16 (last in line) almost always succeeds.
* Middle contestants have increasing chances depending on how much knowledge they gain.

---

## 🔹 Requirements

* Python 3.x
* `random` (built-in, no installation needed)

---

## 🔹 How to Run

Save the script (e.g., `glass_bridge.py`) and run:

```bash
python glass_bridge.py
```

The program will simulate 10,000 trials and print out the **success counts** and **probabilities** for all 16 contestants.

---

## 🔹 Concepts Demonstrated

* Monte Carlo simulation
* Probability estimation
* Impact of order/position on outcomes
* Game theory and risk

---

Do you want me to also **optimize the Simulation function** so it doesn’t keep re-running `Trial()` unnecessarily?

