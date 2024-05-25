import random

# Sample data representing the 100 data points
data = [random.randint(1, 100) for _ in range(100)]

# Function to calculate the profit of a single trade
def calculate_trade_profit(trade, data):
    open_index, close_index = trade
    return data[close_index] - data[open_index]

# Fitness function to calculate the total profit of a strategy
def fitness(strategy, data):
    return sum(calculate_trade_profit(trade, data) for trade in strategy)

# Generate an initial random strategy
def generate_random_trade(data_length):
    open_index = random.randint(0, data_length - 2)
    close_index = random.randint(open_index + 1, data_length - 1)
    return (open_index, close_index)

def generate_initial_population(population_size, strategy_size, data_length):
    return [[generate_random_trade(data_length) for _ in range(strategy_size)] for _ in range(population_size)]

# Tournament selection
def tournament_selection(population, fitnesses, tournament_size):
    selected = random.sample(list(zip(population, fitnesses)), tournament_size)
    selected.sort(key=lambda x: x[1], reverse=True)
    return selected[0][0]

# Single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Mutation operation
def mutate(strategy, data_length, mutation_rate):
    for i in range(len(strategy)):
        if random.random() < mutation_rate:
            strategy[i] = generate_random_trade(data_length)
    return strategy

# Genetic Algorithm
def genetic_algorithm(data, population_size, strategy_size, generations, tournament_size, mutation_rate):
    data_length = len(data)
    population = generate_initial_population(population_size, strategy_size, data_length)
    best_strategy = None
    best_fitness = float('-inf')

    for generation in range(generations):
        fitnesses = [fitness(strategy, data) for strategy in population]
        new_population = []
        
        for _ in range(population_size // 2):
            parent1 = tournament_selection(population, fitnesses, tournament_size)
            parent2 = tournament_selection(population, fitnesses, tournament_size)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1, data_length, mutation_rate)
            offspring2 = mutate(offspring2, data_length, mutation_rate)
            new_population.extend([offspring1, offspring2])
        
        population = new_population
        current_best_fitness = max(fitnesses)
        current_best_strategy = population[fitnesses.index(current_best_fitness)]
        
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_strategy = current_best_strategy
            
        print(f'Generation {generation}: Best Fitness = {best_fitness}')
    
    return best_strategy, best_fitness

# Parameters
population_size = 100
strategy_size = 5
generations = 50
tournament_size = 5
mutation_rate = 0.1

# Run the Genetic Algorithm
best_strategy, best_fitness = genetic_algorithm(data, population_size, strategy_size, generations, tournament_size, mutation_rate)

print('Best Strategy:', best_strategy)
print('Best Fitness:', best_fitness)