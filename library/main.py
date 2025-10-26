from library import Library

library = Library()
    
while True:
    print("------------------------------------")
    print("📚 Library management system")
    print("1. Add a book")
    print("2. Remove a book") 
    print("3. Searching...")
    print("4. Showing all of book you can see")
    print("5. exit")
    print("------------------------------------")
        
    choice = input("Please choose a number for starting ")
    
    if choice == "1":
        title = input("Book title: ")
        author = input("Author name: ")
        library.add_book(title,author)
            
    elif choice == "2":
        title = input("The book you want to delete: ")
        library.remove_book(title)

    elif choice == "3":
        title = input("title for searching: ")
        library.search_book(title)
            
    elif choice == "4":
        library.show_books()
    elif choice == "5":
        exit()        
    else:
        print("Invalid selection")