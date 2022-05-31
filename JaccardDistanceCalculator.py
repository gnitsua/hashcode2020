import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

from Solution import Solution


def get_distance_matrix():
    # solution = Solution.parse_dataset("problem_statement/a_example.txt")
    # solution = Solution.parse_dataset("problem_statement/b_read_on.txt")
    # solution = Solution.parse_dataset("problem_statement/d_tough_choices.txt")
    # solution = Solution.parse_dataset("problem_statement/e_so_many_books.txt")
    # solution = Solution.parse_dataset("problem_statement/f_libraries_of_the_world.txt")
    # distance_matrix = np.zeros((len(solution.libraries), len(solution.libraries)))
    # for x, a in enumerate(solution.libraries):
    #     for y, b in enumerate(solution.libraries):
    #         distance_matrix[x, y] = len(a.books & b.books) / len(a.books | b.books)
    #
    #
    # distance_matrix[distance_matrix == 1] = 0 # set the diagonal to 0 to not obscure data
    # distance_matrix /= np.max(np.abs(distance_matrix), axis=0) # normalize
    # np.save("distances/f", distance_matrix)
    distance_matrix = np.load("distances/f.npy")
    plt.imshow(distance_matrix)
    plt.show()

if __name__ == "__main__":
    get_distance_matrix()
