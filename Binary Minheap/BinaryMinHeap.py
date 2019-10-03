########################################
# PROJECT: Binary Min Heap and Sort
# Author:
########################################

class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []

    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        final = ""
        for i in self.table:
            final += "{" + str(i) + ", " + str(self.table[i]) + "}" + ", "
        return final

    def get_size(self):
        """
        returns the size of the minheap
        :return: size of heap
        """
        return len(self.table)

    def parent(self, position):
        """
        finds the parent of the node
        :param position: the position in the array that the node is in
        :return: the position of the parent
        """

        return (position - 1) // 2

    def left_child(self, position):
        """
        gets the position of the left child of the node, returns None if it doesn't exist
        :param position: the position of the node
        :return: the position of the left child
        """

        return (2 * position) + 1

    def right_child(self, position):
        """
        gets the position of the lright child of the node, returns None if it doesn't exist
        :param position: the position of the node
        :return: the position of the right child
        """

        return (2 * position) + 2

    def has_left(self, position):
        """
        determines if the node has a left child
        :param position: position of the node
        :return: True if left child exists, False if not
        """
        return self.left_child(position) < len(self.table)

    def has_right(self, position):
        """
        determines if the node has a right child
        :param position: position of the node
        :return: True if right child exists, False if not
        """
        return self.right_child(position) < len(self.table)

    def find(self, value):
        """
        finds the index of the node with the value
        :param value: the value to search for
        :return: the index of the node with the value
        """

        for i in self.table:
            if i == value:
                return self.table.index(i)
        return None

    def heap_push(self, value):
        """
        adds a value to the min heap. percolates up if needed
        :param value: value to add to the heap
        :return: Nothing
        """
        if value in self.table:
            return

        self.table.append(value)
        self.percolate_up(len(self.table) - 1)

    def heap_pop(self, value):
        """
        removes a value from the heap,
        :param value:
        :return:
        """
        pos = self.find(value)
        if pos is None:
            return

        self.swap(pos, len(self.table) - 1)
        self.table.pop()
        self.percolate_down(pos)

    def pop_min(self):
        """
        removes and returns the min value in the heap
        :return: the min value in the heap, None if the heap is empty
        """

        if len(self.table) == 0:
            return None
        min_val = self.table[0]
        self.swap(0, len(self.table) - 1)
        self.table.pop()
        if len(self.table) is 0:
            return min_val
        self.percolate_down(0)
        return min_val

    def swap(self, p1, p2):
        """
        swaps elements at indices p1 and p2
        :param p1: index of one node
        :param p2: index of other node
        :return: Nothing
        """
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):
        """
        keeps swapping nodes up until it is in the right place
        :param position: position of the node to start percolating
        :return: Nothing
        """
        parent = self.parent(position)
        while self.table[position] < self.table[parent] and parent >= 0:
            self.swap(position, parent)
            position = parent
            parent = self.parent(position)

    def percolate_down(self, position):
        """
        keeps swapping nodes downward until they are in the right place
        :param position: postition of the node that was just removed and swapped
        :return: Nothing
        """
        if self.has_left(position):
            left = self.left_child(position)
            small_child = left  # although right may be smaller
            if self.has_right(position):
                right = self.right_child(position)
                if self.table[right] < self.table[left]:
                    small_child = right
            if self.table[small_child] < self.table[position]:
                self.swap(position, small_child)
                self.percolate_down(small_child)  # recur at position of small child


def heap_sort(unsorted):
    """
    puts an unsorted list into a min heap and then sorts it
    :param unsorted: the unsorted list
    :return: the sorted list
    """
    heap = BinaryMinHeap()
    n = len(unsorted)
    for i in unsorted:
        heap.heap_push(i)
    temp = []
    for j in range(n):
        val = heap.pop_min()
        temp.append(val)
    return temp
