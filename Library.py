from orderedset import OrderedSet

class Library:
    def __init__(self, id, signup_time, shipping_rate, books = OrderedSet()):
        self.id = id
        self.signup_time = signup_time
        self.shipping_rate = shipping_rate
        self.books = books

    def __str__(self):
        return "%s %s\n%s" % (self.id, len(self.books), " ".join(map(str,self.books)))