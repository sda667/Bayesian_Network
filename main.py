from grid import *
from time import time

if __name__ == "__main__":
    start_time = time()
    grid = Grid(10, [(5, 2), (0, 7), (8, 8)])
    coups = ["D", "R", "R", "R", "R", "D", "R", "D", "D"]
    grid.plot_moves(coups)
    end_time = time()
    print(f"Execution time: {end_time - start_time} seconds")


