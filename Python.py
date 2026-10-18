
N = 4
POPULATION_SIZE = 4

# Initial population
population = [
    [2, 4, 3, 1],
    [1, 2, 3, 4],
    [2, 1, 3, 2],
    [4, 3, 1, 1]
]


def count_conflicts(chromosome):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (chromosome[i] == chromosome[j] or
                    abs(chromosome[i] - chromosome[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


def fitness(chromosome):
    return 1 / (1 + count_conflicts(chromosome))


def roulette_wheel_selection(population, random_numbers):
    fitness_values = [fitness(ch) for ch in population]
    total_fitness = sum(fitness_values)
    probabilities = [f / total_fitness for f in fitness_values]

    print("\nSelection probabilities:")
    for i, probability in enumerate(probabilities):
        print(f"State {i + 1}: {probability:.4f}")

    selected_parents = []

    for r in random_numbers:
        cumulative_probability = 0

        for i, probability in enumerate(probabilities):
            cumulative_probability += probability

            if r < cumulative_probability:
                selected_parents.append(population[i][:])
                break
        else:
            selected_parents.append(population[-1][:])

    return selected_parents


def crossover(parent1, parent2):
    point = 2

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


def evaluate_population(population, generation):
    print("\n" + "=" * 45)
    print(f"GENERATION {generation}")
    print("=" * 45)

    for i, chromosome in enumerate(population):
        conflicts = count_conflicts(chromosome)

        print(
            f"State {i + 1}: {chromosome} | "
            f"Conflicts = {conflicts} | "
            f"Fitness = {fitness(chromosome):.4f}"
        )


def produce_next_generation(population, random_numbers, generation):
    print(f"\nRoulette Wheel Selection for Generation {generation}")

    parents = roulette_wheel_selection(population, random_numbers)

    print("\nSelected parents:")
    for parent in parents:
        print(parent)

    next_generation = []

    for i in range(0, POPULATION_SIZE, 2):
        child1, child2 = crossover(parents[i], parents[i + 1])
        next_generation.extend([child1, child2])

    return next_generation


def main():
    evaluate_population(population, 0)

    # Generation 1
    generation1 = produce_next_generation(
        population,
        [0.10, 0.50, 0.70, 0.90],
        1
    )
    evaluate_population(generation1, 1)

    # Generation 2
    generation2 = produce_next_generation(
        generation1,
        [0.10, 0.35, 0.55, 0.80],
        2
    )
    evaluate_population(generation2, 2)

    best_chromosome = min(generation2, key=count_conflicts)
    best_conflicts = count_conflicts(best_chromosome)

    print("\nFINAL RESULT")
    print("Best chromosome:", best_chromosome)
    print("Number of conflicts:", best_conflicts)

    if best_conflicts == 0:
        print("Solution found!")
    else:
        print("No conflict-free solution found in two generations.")


if __name__ == "__main__":
    main()
