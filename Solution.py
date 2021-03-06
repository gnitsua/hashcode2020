from orderedset._orderedset import OrderedSet

from Library import Library


class Solution:
    def __init__(self, total_days, libraries = []):
        self.libraries = libraries
        self.total_days = total_days
        self.book_scores = {}

    def __str__(self):
        result = "%s\n"%(len(self.libraries))
        for library in self.libraries:
            result += library.__str__() + "\n"

        return result

    def score(self):
        result = 0
        t = 0
        books_scanned = set()
        for library in self.libraries:
            days_to_scan = self.total_days - (t + library.signup_time)
            book_slots = days_to_scan * library.shipping_rate
            for book_count, book in enumerate(library.books):
                if(book_count >= book_slots):
                    break # Out of time for this library
                else:
                    books_scanned = books_scanned.union(set((book,)))
            t += library.signup_time
        for book in books_scanned:
            result += self.book_scores[book]
        return result



    @staticmethod
    def parse_dataset(filepath):
        with open(filepath, "r") as file:
            header_line = file.readline().strip("\n").split(" ")
            assert(len(header_line) == 3)

            result = Solution(int(header_line[2]))

            # Read book scores
            books_line = file.readline().strip("\n").split(" ")
            for book_id, book_score in enumerate(books_line):
                result.book_scores[book_id] = int(book_score)

            # Read each library
            while(True):
                library_info_line = file.readline().strip("\n").split(" ")
                if(library_info_line == None or library_info_line == [""]): # file should end with a blank line
                    break
                assert(len(library_info_line) == 3)
                library_book_line = map(int, file.readline().strip("\n").split(" "))
                result.libraries.append(Library(len(result.libraries),int(library_info_line[1]), int(library_info_line[2]),OrderedSet(library_book_line)))

        return result

    def write_solution(self, filename):
        with open("solutions/%s" % (filename), "w") as file:
            file.write(str(self))