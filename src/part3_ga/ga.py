import random
import numpy as np

class GA:
    def __init__(self, pop_size, cx_rate, mut_rate, fitness_fn, create_ind, max_iters=1000, seed=None):
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        self.pop = [create_ind() for _ in range(pop_size)]
        self.cx_rate = cx_rate
        self.mut_rate = mut_rate
        self.fitness_fn = fitness_fn
        self.max_iters = max_iters

    def select(self, k=2):
        # Seleção por torneio [cite: 386-391]
        cand = random.sample(self.pop, k)
        cand.sort(key=self.fitness_fn, reverse=True)
        return cand[0]

    def crossover(self, p1, p2):
        # Cruzamento aritmético para genes contínuos
        alpha = random.random()
        c1 = alpha * p1 + (1 - alpha) * p2
        c2 = (1 - alpha) * p1 + alpha * p2
        return c1, c2

    def mutate(self, ind):
        # Mutação Gaussiana (ruído nas coordenadas)
        noise = np.random.normal(0, 5.0, size=ind.shape)
        return ind + noise

    def step(self):
        # Evolução de uma geração [cite: 394-418]
        new_pop = []
        while len(new_pop) < len(self.pop):
            p1, p2 = self.select(), self.select()
            c1, c2 = p1.copy(), p2.copy()
            if random.random() < self.cx_rate:
                c1, c2 = self.crossover(c1, c2)
            if random.random() < self.mut_rate:
                c1 = self.mutate(c1)
            if random.random() < self.mut_rate:
                c2 = self.mutate(c2)
            new_pop.extend([c1, c2])
        self.pop = new_pop[:len(self.pop)]

    def run(self):
        # Loop principal [cite: 425-434]
        best = max(self.pop, key=self.fitness_fn)
        for _ in range(self.max_iters):
            self.step()
            cand = max(self.pop, key=self.fitness_fn)
            if self.fitness_fn(cand) > self.fitness_fn(best):
                best = cand
        return best, self.fitness_fn(best)