class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def Availablebooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print('\t *'+ book)
    
    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please keep it safe and return it on time!")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry! This book is unavailable currently. It has either already been issued to someone else or not in our library.") 
            return False
    

    def returnBook(self, bookname):
        self.books.append(bookname)
        print("Thank you for returning this book! We hope you enjoyed reading it.")


class Student:
    def requestBook(self):
        self.book = input("Enter the book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter name of the book you want to return: ")
        return self.book

if __name__ == '__main__':
    student = Student()
    houstoncoleLibrary = Library(['algorithms', 'python','data structures', 'mathematics'])
    # houstoncoleLibrary.Availablebooks()
    while(True):
        initialmsg = ''' ********* WELCOME TO HOUSTON COLE LIBRARY ***********
        Choose one of the options from the following:
        1. Display the list of books
        2. Request for borrowing a book
        3. Return a book
        4. Exit the library

        '''
        print(initialmsg)
        try:
            yourChoice = int(input("Please enter your choice: "))
        
            if yourChoice == 1:
                houstoncoleLibrary.Availablebooks()
            elif yourChoice == 2:
                houstoncoleLibrary.borrowBook(student.requestBook())
            elif yourChoice == 3:
                houstoncoleLibrary.returnBook(student.returnBook())
            elif yourChoice == 4:
                print("Thank you for using Houston Cole Library. Have a great day!")
                exit()
            else:
                print("Invalid choice!")
        except Exception as e:
            e = 'You entered an invalid data. Instead, enter an integer that denotes your choice'
            print(e)
