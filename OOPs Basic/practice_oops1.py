class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"The book title : {self.title} \n The author : {self.author}")

obj1 = Book("Darkness", "Darky")
obj1.display_info()