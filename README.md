# N-Queen Problem Using Genetic Algorithm

## Description
This project solves the 4-Queen problem using a Genetic Algorithm in Python. It uses the given initial population and produces two generations.

## Algorithm Details
- **Population Size:** 4
- **Parent Selection:** Roulette Wheel Selection
- **Crossover:** One-Point Crossover (after the second position)
- **Mutation:** None
- **Fitness:** \(1/(1+\text{number of conflicts})\) for selection

## Features
- Counts conflicts between queens in the same row or diagonal.
- Calculates fitness and selection probabilities.
- Generates two generations using crossover.
- Displays each generation and its conflicts.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Run the following command:

```bash
python assignment2.py
```

## Output
The program displays the initial population, both generated generations, their conflicts and fitness values, and the best chromosome found after two generations.

## Conclusion
This project demonstrates how a Genetic Algorithm can be used to solve the N-Queen problem using selection and crossover.
