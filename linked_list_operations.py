class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def addition(self):
        current_node = self.head
        total = 0
        while current_node:
            total += current_node.data
            current_node = current_node.next
        return total

    def subtraction(self):
        current_node = self.head
        if current_node is None:
            return 0
        total = current_node.data
        current_node = current_node.next
        while current_node:
            total -= current_node.data
            current_node = current_node.next
        return total

    def multiplication(self):
        current_node = self.head
        if current_node is None:
            return 0
        total = current_node.data
        current_node = current_node.next
        while current_node:
            total *= current_node.data
            current_node = current_node.next
        return total

def main():
    linked_list = LinkedList()

    print("Enter numbers (enter 'q' to quit):")
    while True:
        user_input = input()
        if user_input.lower() == 'q':
            break
        try:
            num = int(user_input)
            linked_list.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")

    print("Numbers in the linked list:")
    linked_list.print_list()

    print("Select an operation (+, -, *):")
    operation = input()

    if operation == '+':
        result = linked_list.addition()
        print("Sum:", result)
    elif operation == '-':
        result = linked_list.subtraction()
        print("Difference:", result)
    elif operation == '*':
        result = linked_list.multiplication()
        print("Product:", result)
    else:
        print("Invalid operation. Please try again.")

if __name__ == "__main__":
    main()
