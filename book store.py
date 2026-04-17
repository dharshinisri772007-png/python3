library_books = ["Harry Potter", "Wings of Fire", "Bascic of Python","AI Introduction"]
borrowed_books = []
def display_books():
 print("\nAvailable Books:")
 for book in library_books:
    print("-", book)
def display_borrowed():
 print("\nBorrowed Books:")
 if borrowed_books:
   for book in borrowed_books:
     print("-", book)
 else:
   print("No books borrowed")
def borrow_book():
 book = input("\nEnter book name to borrow: ")
 if book in library_books:
   library_books.remove(book)
 borrowed_books.append(book)
 print("You borrowed:", book)
 print("Book not available")
def return_book():
 book = input("\nEnter book name to return: ")
 if book in borrowed_books:
  borrowed_books.remove(book)
 library_books.append(book)
 print("Book returned:", book)
 print("This book was not borrowed")
def menu():
 while True:
  print("\n===== Library Menu =====")
  print("1. View Available Books")
  print("2. Borrow Book")
  print("3. Return Book")
  print("4. View Borrowed Books")
  print("5. Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
   display_books()
  elif choice == "2":
   borrow_book()
  elif choice == "3":
   return_book()
  elif choice == "4":
   display_borrowed()
  elif choice == "5":
    print("Thank you for using the Library System")
  break
 else:
  print("Invalid choice")
menu()