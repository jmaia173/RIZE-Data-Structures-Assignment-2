# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''

    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        return f"{name} added to the front of the waitlist"

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        print("Current waitlist:")
        current = self.head
        while current is not None:
            print(f"- {current.name}")
            current = current.next

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
            return f"{name} added to the end of the waitlist"

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        if self.head is None:
            return f"{name} not found"

        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return f"Removed {name} from the waitlist"
            current = current.next

        return f"{name} not found"


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            print(waitlist.add_front(name))

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            print(waitlist.add_end(name))

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            print(waitlist.remove(name))

        elif choice == "4":
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Call the waitlist_generator function to start the program
waitlist_generator()


'''
Design Memo

How does your list work?
My waitlist is a singly linked list built from two classes. A Node stores a customer's name and a next pointer to the following Node (or None at the end). The LinkedList class stores only a head pointer to the first Node. add_front creates a Node, points its next at the current head, then makes it the new head, which takes constant time. add_end walks to the last Node and links the new Node there, which takes time proportional to the list length. remove walks the list looking for a matching name. If the match is the head, head moves to the second Node; otherwise the previous Node's next skips over the match. print_list walks from head to the end and prints each name, or reports an empty waitlist.

What role does the head play?
The head is the only entry point into the list. If it is lost, every Node becomes unreachable. It also defines who is first in line: adding a VIP means changing head, and removing the first customer means moving head to the next Node. An empty list is simply head being None, which is why each method checks for that case.

When might a real engineer need a custom list like this?
A custom list gives full control over ordering and insertion. A ticketing team might need VIPs who jump the line, customers who cancel from the middle, or entries that track extra data like timestamps and priority tiers. A built-in Python list shifts every element after a front insertion, while a linked list only updates a pointer. Custom linked structures also appear in memory allocators, undo histories, and LRU caches.
'''