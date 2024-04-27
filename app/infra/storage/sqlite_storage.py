import sqlite3
from domain.book import Book

class SQLiteStorage:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                publish_year INTEGER,
                pages_count INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def add(self, book):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO books (title, description, publish_year, pages_count, created_at)
            VALUES (?, ?, ?, ?, ?)
        ''', (book.title, book.description, book.publish_year, book.pages_count, book.created_at))
        self.conn.commit()
        return cursor.lastrowid

    def delete(self, id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (id,))
        self.conn.commit()

    def get(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        return [Book(*row[1:]) for row in rows]