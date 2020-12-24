# library management system
# add a book
# return a book
# lend book (who owns the book if not present)
# display book

class library:
    def __init__(self, listofbooks, type, book_id):
        self.list_of_books = listofbooks
        self.book_type = type
        self.book_id = book_id
    if __name__=="__main__":
        while True:
            print("BOOKS LIBRARY")
            print("Please select option between the given option")
            print("1. Add book\n 2. Buy book\n 3.Display book\n 4. Exit\n")
            n = int(input("Choose your option: "))
            list_of_books =["Python", "Data structure", "Google Adword"]
            if (n==1):
                num = int(input("Enter the number of books you want to add: "))
                i = 0
                while(i<num):
                    i+=1
                    list_of_books.append(input("Enter book Name: "))

            elif(n==2):
                num1 = input("Enter book name: ")
                if (num1 in list_of_books):
                    list_of_books.remove(num1)
                    print("Buying Successfully.....")
                else:
                    print("Book is not available.....")
            elif(n==3):
                item = input("Enter book name: ")
                if item in list_of_books:
                    print("Here is the book",item)
                else:
                    print("Sorry we dont have the book.....")
            else:
                print("Thank you for using our library...****")
                break

            print("List of books", list_of_books)
    def details(self):
        return  f"Books are {self.list_of_books}, books type {self.book_type} books id {self.book_id}"

Ashu_library = library(["Python", "Data structure", "Google Adword"], ["Technical", "IT"], 56)
print(Ashu_library.details())