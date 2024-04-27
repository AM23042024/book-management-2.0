from domain.book import Book


class MemoryStorage:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)
        return len(self.books) - 1

    def delete(self, id):
        del self.books[int(id)]
    
    def get(self):
        return self.books
