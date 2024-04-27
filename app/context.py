from infra.storage.sqlite_storage import SQLiteStorage

class Context:
    def __init__(self):
        book_storage = SQLiteStorage("test.db")
        self.book_service = BookService(book_storage)