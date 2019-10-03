########################################
# PROJECT 1 - Linked List
# Author:
# PID:
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)


class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None  # Node
        self.tail = None  # Node
        self.size = 0  # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    ###### MODIFY THE BELOW FUNCTIONS #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        Gets the number of nodes of the linked list
        :return: size of list
        """
        return self.size

    def is_empty(self):
        """
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        """
        if self.size == 0:
            return True
        else:
            return False

    def front_value(self):
        """
        Gets the first value of the list
        :return: value of the list head
        """
        if self.head is None:
            return None
        else:
            return self.head.value

    def back_value(self):
        """
        Gets the last value of the list
        :return: value of the list tail
        """
        if self.tail is None:
            return None
        else:
            return self.tail.value

    def count(self, val):
        """
        Counts the number of times a value 'val' occurs in the list
        :param val: value to find and count
        :return: number of time 'val' occurs
        """

        count = 0
        temp_node = self.head
        while temp_node is not None:  # iterates through the LinkedList
            if temp_node.value == val:
                count += 1
            temp_node = temp_node.next_node
        return count

    def find(self, val):
        """
        Searches for and returns the first node with the value 'val'
        :param val: value to search for
        :return: True if value is in list, False if value is not found
        """
        temp_node = self.head
        while temp_node is not None:  # iterates through the LinkedList
            if temp_node.value == val:
                return True
            temp_node = temp_node.next_node
        return False

    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        Adds a node to the front of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        temp_node = Node(int(val))
        if self.head is None:  # if list is empty
            self.head = temp_node
            self.tail = temp_node
            self.size += 1
        else:
            temp_node.next_node = self.head
            self.head = temp_node
            self.size += 1

    def push_back(self, val):
        """
        Adds a node to the back of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        val_node = Node(int(val))
        if self.head is None:  # if list is empty
            self.head = val_node
            self.tail = val_node
            self.size += 1
        else:
            val_node.next_node = None
            self.tail.next_node = val_node
            self.tail = val_node
            self.size += 1

    def pop_front(self):
        """
        Removes a node from the front of the list
        :return: the value of the removed node
        """
        if self.head is None:
            return None
        else:
            popped = self.head  # node that was removed
            self.size -= 1
            self.head = self.head.next_node
            return popped.value

    def pop_back(self):
        """
        Removes a node from the back of the list
        :return: the value of the removed node
        """
        if self.tail is None:
            return None
        if self.tail == self.head:
            popped = self.head
            self.head = None
            self.tail = None
            self.size = 0
            return popped.value
        else:
            popped = self.tail
            temp_node = self.head
            while temp_node is not None:  # iterates through the LinkedList
                if temp_node.next_node == self.tail:
                    self.tail = temp_node
                    self.size -= 1
                    self.tail.next_node = None
                    return popped.value
                temp_node = temp_node.next_node

    def reverse_list(self):
        """
        Reverses the values of the given linked list
        :return: no return
        """
        reverse_list = LinkedList()
        temp_node = self.head
        while temp_node is not None:  # iterates through the LinkedList
            reverse_list.push_front(temp_node.value)  # fills the empty LinkedList with the values in reverse order
            temp_node = temp_node.next_node
        self.head = reverse_list.head
        self.tail = reverse_list.tail
