# class Queue:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.items = []

#     def enqueue(self, item):
#         if self.is_full():
#             print("Queue is Full!")
#         else:
#             self.items.append(item)
#             print(item, "Added to Queue")

#     def is_full(self):
#         return len(self.items) == self.capacity

#     def dequeue (self):
#         if self.is_empty():
#             print("Queue is Empty!")
#             return None
#         else:
#             item = self.items.pop(0)
#             print(item, "Removed from Queue")
#             return item

#     def is_empty(self):
#         return len(self.items) == 0

#     def peek(self):
#         if self.is_empty():
#             print("Queue is Empty!")
#             return None
#         else:
#             return self.items[0]

#     def display(self):
#         print(self.items)



# queue = Queue(10)
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# queue.enqueue(8)
# queue.enqueue(9)
# queue.enqueue(10)
# queue.enqueue(11)
# queue.enqueue(12)

# queue.dequeue()

# print(queue.peek(), "Is next in line.")

# queue.display()

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full!")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data

        print(data, "Added to Queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None

        data = self.front == self.rear
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) %  self.capacity
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        return self.queue[self.front]

    def next(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        return self.queue[self.front + 1]

    def display(self):
        if self.is_empty():
            print("Queue is Empty!")
            return None
        else:
            print("Queue    :",self.queue)

list = CircularQueue(5)
while True:
    print("="*22)
    print("Hospital Queue System")
    print("="*22)
    print("1. Register Patient\n2. Call Next Patient\n3. View Next Patient\n4. Display Waiting Patients\n5. Check Empty\n6. Check Full\n7. Exit")
    print("="*22)
    choice = input("Action    : ")
    if choice.isdigit():
        if choice == "1":
            name = input("Name of Patient: ")
            num = input("Patient Number: ")
            visit_for = input("Visiting for/symtoms: ")
            patient_info = (name + " | " + num + " | " + visit_for)
            data = patient_info
            list.enqueue(data)
        if choice == "2":
            done = list.peek()
            print(done, "| Has been successfuly discharged.")
            done = list.dequeue()
            next = list.peek()
            print(next, "| Has been called in.")
        if choice == "3":
            next = list.next()
            print(next, "| Is the next patient in line.")
        if choice == "4":
            list = list.display()
            print(list, "| Current Queue.")
        if choice == "5":
            if list.is_empty():
                print("No patients is queue.")
            else:
                print("There are patient/s in queue.")
        if choice == "6":
            if list.is_full():
                print("List if full can't admit more.")
            else:
                print("List has not exceeded capacity")
        if choice == "7":
            print("Exiting...")
            print("Exited successfuly!")
            break
    else:
        print("Invalid Input/Range!")