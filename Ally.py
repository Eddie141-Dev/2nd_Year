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
      print("Queue is full")
      return
    if self.is_empty():
      self.front = 0
    self.rear = (self.rear + 1) % self.capacity
    self.queue[self.rear] = data

    print(data, "added to queue.")
  def dequeue(self):
    if self.is_empty():
      print("Queue is empty")
      return None

    data = self.queue[self.front]
    self.queue[self.front] = None

    if self.front == self.rear:
      self.front = -1
      self.rear = -1
    else:
      self.front = (self.front + 1) % self.capactiy
    return data

  def peek(self):
    if self.is_empty():
      print("Queue is empty")
    return self.queue[self.front]

  def display(self):
    if self.is_empty():
      print("Queue is empty")
    else:
      print("Queue: ", self.queue)

queue1 = CircularQueue(10)
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
queue1.enqueue(40)
queue1.enqueue(50)
queue1.enqueue(60)
queue1.display()

queue1.enqueue(60)