class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
       
        self.items = self.items + [x]
        print(f"Successfully pushed '{x}' onto the stack.")

    def pop(self):
       
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        
        top_element = self.items[-1]
       
        self.items = self.items[:-1]
        print(f"Popped element: {top_element}")
        return top_element

    def peek(self):
       
        if self.is_empty():
            print("Stack is empty.")
            return None
        
        print(f"Top element: {self.items[-1]}")
        return self.items[-1]

    def is_empty(self):
       
        return len(self.items) == 0

    def display(self):
       
        if self.is_empty():
            print("Current Stack: [] (Empty)")
        else:
            print(f"Current Stack (Bottom -> Top): {self.items}")


def main():
    stack = Stack()

    while True:
        print("\n=== STACK OPERATIONS MENU ===")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            element = input("Enter element to push: ")
            stack.push(element)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
