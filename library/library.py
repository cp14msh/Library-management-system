class Library:
    def __init__(self):
        self.book = []

    def add_book(self,title,author):
        if title in self.book:
            print("You already added this book")
        else:
            self.book.append({"title": title , "author": author})

    def remove_book(self, title):
        for book in self.book:
            if book["title"]==title:
                self.book.remove(book)
                print(f"{book} was removed.")
            else:
                print("We don't have this book in our library")


    def search_book(self,title):
        if title in self.add_book:
            print(f"finded, its author is {self.book["author"]}")
        else:
            print("couldn't find this book!")

    def show_books(self):
        for _ in self.book:
            print (_)
