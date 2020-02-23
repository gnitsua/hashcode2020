import numpy as np

from Library import Library
from Solution import Solution
import skopt


def main(max_score_weight, signup_weight, shipping_rate_weight):
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

    # MAX_LIBRARY_SCORE = solution.max_library_score()
    MAX_LIBRARY_SCORE = 412714

    # MAX_SIGNUP_TIME = solution.max_sign_up_time()
    MAX_SIGNUP_TIME = 300

    # MAX_SHIPPING_RATE = solution.max_shipping_rate()
    MAX_SHIPPING_RATE = 10

    for library in solution.libraries:
        library.books = list(library.books)
        library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
        # print(library.max_score(solution.book_scores)/MAX_LIBRARY_SCORE, 1 - library.signup_time/MAX_SIGNUP_TIME, library.shipping_rate/MAX_SHIPPING_RATE)

    solution.libraries.sort(key=lambda library:
        max_score_weight * library.max_score(solution.book_scores)/MAX_LIBRARY_SCORE +
                           signup_weight * 1 - library.signup_time/MAX_SIGNUP_TIME +
                            shipping_rate_weight * library.shipping_rate/MAX_SHIPPING_RATE , reverse=True)
    score = solution.score()
    print(score)
    return score
    # solution.write_solution("F-%s.txt" % score)

SPACE = [skopt.space.Real(0,1.0, name="max_score_weight"),
             skopt.space.Real(0, 1.0, name="signup_weight"),
             skopt.space.Real(0, 1.0, name="shipping_rate_weight")]

@skopt.utils.use_named_args(SPACE)
def objective(**params):
    return 10000000.0 - main(**params)

if __name__ == "__main__":
    results = skopt.forest_minimize(objective, SPACE)
    print(results)
    print(results.x)
    print(main(results.x[0],results.x[1],results.x[2]))
