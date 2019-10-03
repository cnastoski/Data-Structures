"""
# Project 4
# Name: Chris Nastoski
# PID: A53276668
"""


class Stack:
    """
    Stack class
    """

    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        """
        :return: The size of the stack
        """
        return self.size

    def is_empty(self):
        """
        Checks to see if the stack is empty
        :return: True if it is empty
        """
        return True if (self.size == 0) else False

    def top(self):
        """
        Takes the last value added and just displays it
        :rtype: object
        :return: the last data added to the stack
        """
        return self.data[self.size - 1]

    def push(self, val):
        """
        adds a value to the stack
        :param val: the value to be added
        :return: Nothing
        """
        if self.capacity == self.size:
            self.grow()

        self.data[self.size] = val
        self.size += 1

    def pop(self):
        """
        removes the last value added to the stack
        :return: the last value added
        """
        if self.size == 0:
            return None

        val = self.top()
        self.data[self.size - 1] = None
        self.size -= 1
        if self.size <= self.capacity // 2 and self.capacity > 3:
            self.shrink()
        return val

    def grow(self):
        """
        doubles the stack capacity if the capacity is reached
        :return: Nothing
        """
        self.data += [None] * self.capacity
        self.capacity *= 2

    def shrink(self):
        """
        shrinks the stack capacity if the size falls below half of the capacity
        :return: Nothing
        """
        self.capacity = self.capacity // 2
        self.data = [value for value in self.data if value not in [None] * self.capacity]
        # list comprehension should still be O(n) time complexity


def reverse(stack):
    """
    reverses all values in a stack
    :param stack: the stack to reverse
    :return: the reversed stack
    """
    temp = Stack()
    for i in range(stack.size):
        temp.push(stack.pop())
    return temp


def replace(stack, old, new):
    """
    replaces all instances of a value in a stack with the new value
    :param stack: the stack to replace values
    :param old: the value to be replaced
    :param new: the new value to take old's place
    :return: the stack with replaced values
    """
    temp = Stack()
    for i in range(stack.size):
        if stack.top() == old:
            stack.pop()
            temp.push(new)
        else:
            temp.push(stack.pop())
    del stack
    return reverse(temp)


