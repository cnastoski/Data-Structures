class CircularQueue:
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        """
        (Not tested but I love clean code)
        used by the print statement to represent the queue
        :return: the queue data
        """
        queue = ""
        if self.size == 0:
            return "None"
        for i in range(len(self.data)):
            queue += (str(self.data[i]) + ", ")
        return queue[:-2]

    def is_empty(self):
        """
        checks to see if the queue is empty
        :return: True if it it empty
        """
        return True if self.size == 0 else False

    def __len__(self):
        """
        :return: The length of the queue
        """
        return self.size

    def first_value(self):
        """
        :return: the value at the front of the line
        """
        return self.data[self.head]

    def enqueue(self, val):
        """
        adds a value to the end of the line. grows the queue if necessary. Loops around the array to fill the queue
        :param val: the value to add to the line
        :return: Nothing
        """
        self.data[self.tail] = val
        self.size += 1
        if len(self.data) == self.size:
            self.grow()
        self.tail = (self.head + self.size) % len(self.data)

    def dequeue(self):
        """
        removes the value at the front of the line and shrinks the queue if necessary
        :return: The value removed at the front of the line
        """
        if self.is_empty():
            return None
        val = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)  # the head loops around the queue in a circular manner
        self.size -= 1
        if (self.size <= (self.capacity // 4)) and (self.capacity > 4):
            self.shrink()
        return val

    def grow(self):
        """
        Doubles the size of the queue if it reaches capacity
        :return: Nothing
        """
        self.capacity *= 2
        temp = [None] * self.capacity
        for k in range(len(self.data)):
            temp[k] = self.data[self.head]
            self.head += 1
        self.head = 0
        self.data = temp
        self.tail = (self.head + self.size) % len(self.data)

    def shrink(self):
        """
        halves the size of the queue if the size falls below 25% of the capacity
        :return: Nothing
        """
        self.capacity = self.capacity // 2
        temp = [None] * self.capacity
        for k in range(len(self.data)):
            if self.data[self.head] is not None:
                temp[k] = self.data[self.head]
                self.head += 1
        self.head = 0
        self.data = temp
        self.tail = (self.head + self.size) % len(self.data)
