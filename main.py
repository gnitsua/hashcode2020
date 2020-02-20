import numpy as np

from Library import Library
from Solution import Solution


def main():
    solution = Solution.parse_dataset("problem_statement/a_example.txt")
    solution.libraries.reverse()
    solution.libraries[0].books.remove(0)
    print("A: %s" % solution.score())
    solution.write_solution("A.txt")


if __name__ == "__main__":
    main()
