import numpy as np
import itertools
import math
import random
import matplotlib.pyplot as plt


def distance(coord_a, coord_b):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(coord_a, coord_b)))


class BayesianNetwork:
    def __init__(self, grid_size, num_gems):
        self.grid_size = grid_size
        self.num_gems = num_gems
        self.G = [[1 / (grid_size ** 2) for _ in range(grid_size)] for _ in range(grid_size)]

    def likelihood(self, observed_distances, predicted_distances):
        d = sum((o - p) ** 2 for o, p in zip(observed_distances, predicted_distances))
        return math.exp(-d * 0.3)

    def infer(self, agent_position, observed_distances):
        new_beliefs = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        possible_positions = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size)]
        all_permutations = itertools.permutations(possible_positions, self.num_gems)
        for gem_positions in all_permutations:
            predicted_distances = [distance(agent_position, gem_position) for gem_position in gem_positions]
            likelihood_value = self.likelihood(observed_distances, predicted_distances)
            for x, y in gem_positions:
                new_beliefs[x][y] += self.G[x][y] * likelihood_value

        for x in range(self.grid_size):
            for y in range(self.grid_size):
                new_beliefs[x][y] = 0.9 * new_beliefs[x][y] + 0.1 * self.G[x][y]
        total = sum(sum(row) for row in new_beliefs)
        if total > 0:
            self.G = [[new_beliefs[x][y] / total for y in range(self.grid_size)] for x in range(self.grid_size)]
        else:
            self.G = new_beliefs

    def get_belief_distribution(self):
        return np.array(self.G)


