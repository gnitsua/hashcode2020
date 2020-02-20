import numpy as np

from Library import Library
from Solution import Solution


def main():
    solution = Solution.parse_dataset("problem_statement/d_tough_choices.txt")
    for library in solution.libraries:
        library.books = list(library.books)
        library.books.sort(key=lambda book: solution.book_scores[book], reverse=True)
    solution.libraries.sort(key=lambda library: (sum(library.books)*library.shipping_rate**1.25)/(library.signup_time**1.9), reverse=True)
    solution.write_solution("D-%s.txt" % solution.score())

if __name__ == "__main__":
    main()
