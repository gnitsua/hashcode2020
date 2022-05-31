import numpy as np

from Library import Library
from Solution import Solution
import skopt
from skopt.plots import plot_evaluations
import matplotlib.pyplot as plt

def main():
    solution = Solution.parse_dataset("problem_statement/f_libraries_of_the_world.txt")

    # solution.libraries.reverse()
    # solution.libraries.sort(key=lambda library: library.signup_time)
    # solution.libraries.sort(key=lambda library: library.signup_time, reverse=True)
    # solution.libraries.sort(key=lambda library: library.shipping_rate)

    # for library in solution.libraries:
    #     library.books = list(library.books)
    #     library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
    # solution.libraries.sort(key=lambda library: library.signup_time)

    # for library in solution.libraries:
    #     library.books = list(library.books)
    #     library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
    # solution.libraries.sort(key=lambda library: sum(library.books)/library.signup_time, reverse=True)

    # for library in solution.libraries:
    #     library.books = list(library.books)
    #     library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
    # solution.libraries.sort(key=lambda library: (sum(library.books)*library.shipping_rate)/(library.signup_time), reverse=True)

    # for library in solution.libraries:
    #     library.books = list(library.books)
    #     library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
    # solution.libraries.sort(key=lambda library: (sum(library.books))/(library.signup_time), reverse=True)

    # for library in solution.libraries:
    #     library.books = list(library.books)
    #     library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
    # solution.libraries.sort(key=lambda library: (library.shipping_rate) / (library.signup_time), reverse=True)

    # for library in solution.libraries:
    #     library.books = list(library.books)
    #     library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
    # solution.libraries.sort(key=lambda library: (sum(library.books)*library.shipping_rate)/(library.signup_time**2), reverse=True)

    # distance_matrix = np.load("distances/a.npy")
    # average_distance = np.mean(distance_matrix, axis=1)
    SPACE = [skopt.space.Integer(750, 1000, name="max_score_weight"),
             skopt.space.Integer(0, 1000, name="signup_weight"),
             skopt.space.Integer(0, 1000, name="shipping_rate_weight")]

    @skopt.utils.use_named_args(SPACE)
    def objective(**params):
        solution.sort(**params)
        return -solution.score()


    # results = skopt.gp_minimize(objective, SPACE, n_jobs=-1, n_calls=200, n_random_starts=100, verbose=True, xi=10000)
    # print(results)
    # print(results.x)
    solution.sort(1, 1000, 1000)
    print(solution.score())
    # _ = skopt.plots.plot_evaluations(results, bins=10)

    # plt.savefig('results.png')

    # plt.show()


    # if(save == True):
    #     solution.write_solution("F-%s.txt" % score)



if __name__ == "__main__":
    main()