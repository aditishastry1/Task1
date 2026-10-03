class Item:
    
    
    def __init__(self, title: str):
       
        self.__title = title
        self.__is_borrowed = False

    @property
    def title(self) -> str:
        
        return self.__title

    @property
    def is_borrowed(self) -> bool:
        
        return self.__is_borrowed

    def borrow(self) -> bool:
        
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_item(self) -> None:
        
        self.__is_borrowed = False

    def __str__(self) -> str:
       
        status = "Borrowed" if self.__is_borrowed else "Available"
        return f"Item: '{self.__title}' [{status}]"


class Book(Item):
        def __init__(self, title: str, author: str, pages: int):
        super().__init__(title)
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        
        return f"Book: '{self.title}' by {self.author} ({self.pages} pages)"


class DVD(Item):
        def __init__(self, title: str, duration_minutes: int):
        super().__init__(title)
        self.duration_minutes = duration_minutes

    def __str__(self) -> str:
        
        return f"DVD: '{self.title}' ({self.duration_minutes} mins)"


class Library:
    

    def __init__(self):
        self.items = []

    def add_item(self, item: Item) -> None:
        
        self.items.append(item)

    def borrow_item(self, title: str) -> None:
      
        for item in self.items:
            if item.title.lower() == title.lower():
                if not item.borrow():
                    print(f"Sorry, '{item.title}' is already borrowed.")
                return
        print(f"Item '{title}' not found in the library.")

    def show_available(self) -> None:
        """Prints all items currently available for borrowing."""
        print("Available Items:")
        for item in self.items:
            if not item.is_borrowed:
               
                print(item)



if __name__ == "__main__":
    lib = Library()
    
    
    lib.add_item(Book("Atomic Habits", "James Clear", 320))
    lib.add_item(DVD("Inception", 148))
    
  
    lib.borrow_item("Inception")
    
   
    lib.show_available()
