class Library:
    def _init_(self):
        self.books = []

    def add_book(self, title, author, year, genre, read_status):
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status
        }
        self.books.append(book)
        return f'📚 "{title}" added successfully!'

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                return f'❌ "{title}" removed successfully!'
        return f'⚠️ Book "{title}" not found.'

    def search_books(self, query, by="title"):
        return [book for book in self.books if query.lower() in book[by].lower()]

    def get_books(self):
        return self.books

    def get_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book["read_status"])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
        return total_books, round(percentage_read, 2)