class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

    def push(self, data):
        if self.top == None:
            self.top = Node(data)
        else:
            new_top = Node(data)
            new_top.next = self.top
            self.top = new_top

    def pop(self):
        if self.is_empty():
            return None
        else:
            poppednode = self.top
            self.top = self.top.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.data

    def display(self):
        next_top = self.top
        if self.is_empty():
            print("Stack Underflow")
        else:
            while(next_top != None):
                print(next_top.data, end="")
                next_top = next_top.next
                if(next_top != None):
                    print(" -> ", end="")
            return

list = Stack()

while True:
  print("="*23)
  print("Stack Using Linked List")
  print("="*23)
  print("1. Push\n2. Pop\n3. Peek\n4. Display\n5. Check if Empty\n6. Exit")
  print("="*23)
  choice = input("Select Action: ")
  if choice.isdigit():
    if choice == "1":
      add = input("What do you want to add? ")
      add.strip
      list.push(add)
      list.display()
    if choice == "2":
      print("Removing the most reccent addition")
      list.pop()
      list.display()
    if choice == "3":
      print(f"Latest addition: {list.peek()}")
    if choice == "4":
      list.display()
    if choice == "5":
      if list.is_empty():
        print("Stack is Empty")
        list.display()
      else:
        print("Stack is Filled")
        list.display()
    if choice == "6":
      print("Exting...")
      print("Exited Succsesfully!")
      break
  else:
    print("Not a valid number or out of range")
