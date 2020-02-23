import numpy as np

from Library import Library
from Solution import Solution


def main():
    solution = Solution.parse_dataset("problem_statement/b_read_on.txt")
    distance_matrix = np.zeros((len(solution.libraries), len(solution.libraries)))
    for x, a in enumerate(solution.libraries):
        for y, b in enumerate(solution.libraries):
            distance_matrix[x, y] = len(a.books & b.books) / len(a.books | b.books)

    print(distance_matrix)
    # for library in solution.libraries:
    #     library.books = list(library.books)
    #     library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
    # solution.libraries.sort(key=lambda library: (sum(library.books)*library.shipping_rate**1.25)/(library.signup_time**1.9), reverse=True)
    # solution.write_solution("B-%s.txt" % solution.score())

if __name__ == "__main__":
    main()
