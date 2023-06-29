import random


class GeneticAlgorithm:

    def __init__(self, population_size, crossover_rate, mutation_rate, source_gene, iteration_count=-1, target_fitness=1):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.source_gene = source_gene
        self.iteration_count = iteration_count
        self.target_fitness = target_fitness
        self.gene_length = len(source_gene)
        self.population = []
        self.fitness_values = []
        self.avg_fitness_per_generation = []
        self.max_fitness_per_generation = []

    def create_population(self):
        self.population = [self.create_gene()
                           for _ in range(self.population_size)]
        self.fitness_values = [self.calculate_fitness_value(
            gene) for gene in self.population]

    def create_gene(self):
        return [random.randint(0, 1) for _ in range(self.gene_length)]

    def calculate_fitness_value(self, gene):
        return sum(g != t for g, t in zip(gene, self.source_gene)) / self.gene_length

    def make_selection(self):
        return self.biased_selection() if random.random() < 0.5 else self.tournament_selection()

    def biased_selection(self):
        total_fitness = sum(self.fitness_values)
        probs = [fitness / total_fitness for fitness in self.fitness_values]
        return random.choices(self.population, weights=probs, k=2)

    def tournament_selection(self):
        return random.sample(self.population, 2)

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.gene_length - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        else:
            return parent1, parent2

    def mutate(self, gene):
        return [1 - v if random.random() < self.mutation_rate else v for v in gene]

    def run(self):
        self.create_population()

        generation_count = 0

        while not (1 in self.fitness_values or generation_count == self.iteration_count or max(self.fitness_values) >= self.target_fitness):

            new_population = []
            for _ in range(self.population_size):
                parent1, parent2 = self.make_selection()
                childs = self.crossover(parent1, parent2)
                child1 = self.mutate(childs[0])
                child2 = self.mutate(childs[1])
                new_population.extend([child1, child2])

            new_population.sort(key=self.calculate_fitness_value)
            new_population = new_population[self.population_size:]
            # print(len(new_population))

            self.max_fitness_per_generation.append(max(self.fitness_values))
            self.avg_fitness_per_generation.append(
                sum(self.fitness_values)/self.gene_length)

            self.population = new_population
            self.fitness_values = [self.calculate_fitness_value(
                gene) for gene in self.population]

            generation_count += 1

        best_gene = self.population[self.fitness_values.index(
            max(self.fitness_values))]

        return best_gene, generation_count, max(self.fitness_values)
