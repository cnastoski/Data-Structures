class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    def insert(self, value):
        """
        inserts a node into the tree with the given value
        :param value: the value to insert
        :return: nothing, just adds to the tree
        """
        if self.root is None:  # empty tree
            new = Node(value)
            self.root = new
            self.size += 1
            return 0
        current = self.root
        while current.value is not None:
            # goes through the tree trying to find the next leaf
            if value == current.value:
                return 0

            if value > current.value:
                if current.right is None:
                    new = Node(value, current)
                    current.right = new
                    self.size += 1
                    return 0
                current = current.right

            if value < current.value:
                if current.left is None:
                    new = Node(value, current)
                    current.left = new
                    self.size += 1
                    return 0
                current = current.left

    def remove(self, value):
        """
        takes a value of a node to remove and finds the node and removes it
        :param value: the value of the node to be removed
        :return: Nothing
        """
        if self.root is None:  # case with no root
            return None
        target = self.search(value, self.root)
        if target.value != value:  # case where the node doesn't exist
            return None

        if target is self.root:
            # cases where the root is the one being removed
            if not self.root.left and not self.root.right:
                self.root = None

                return None

            if self.root.right and not self.root.left:
                self.root = self.root.right
                self.root.parent = None

                return None
            if self.root.left and not self.root.right:
                self.root = self.root.left
                self.root.parent = None

                return None
            if self.root.right and self.root.right:
                replacement = self.min(self.root.right)
                val = replacement.value
                self.remove(replacement.value)
                self.root.value = val
                return None

        isl = self.is_left(target)
        # checks for which side of the parent it is on
        if not target.left and not target.right:  # case with no children
            if isl:
                target.parent.left = None
            else:
                target.parent.right = None

        if target.left and not target.right:  # only left child exists
            if isl:
                target.parent.left = target.left
                target.left.parent = target.parent

            else:
                target.parent.right = target.left
                target.left.parent = target.parent

        if not target.left and target.right:  # only right child exists
            if isl:
                target.parent.left = target.right
                target.right.parent = target.parent

            else:
                target.parent.right = target.right
                target.right.parent = target.parent

        if target.left and target.right:  # both children exist
            replacement = self.min(target.right)
            if self.is_leaf(replacement):
                val = replacement.value
                self.remove(replacement.value)
                target.value = val
            else:
                target.value = replacement.value
                replacement.parent.right = replacement.right
                replacement.right.parent = replacement.parent
        self.size = self.count(self.root)

    def is_left(self, node):
        """
        checks to see if the node is a left child
        :param node: node to check
        :return: True if it is a left child, False if right child
        """
        if node.parent.left == node:
            return True
        return False

    def search(self, value, node):
        """
        searches for the node with the value
        :param value: the value to search for in the tree
        :param node: the the root to start with
        :return: the node with the value, Nothing if it is not in the tree
        """
        if node is None:
            return None
        if node.value == value:
            return node
        if value > node.value:
            if node.right is None:
                return node
            return self.search(value, node.right)
        if value < node.value:
            if node.left is None:
                return node
            return self.search(value, node.left)

    def inorder(self, node):
        """
        Creates a generator object with all of the nodes sorted in an inorder 
        traversal
        :param node: the root to start with
        :return: a generator with all of the nodes
        """
        if node is not None:
            yield from self.inorder(node.left)
            yield node.value
            yield from self.inorder(node.right)

    def preorder(self, node):
        """
        same as inorder but with a preorder traversal
        :param node: the root to start with
        :return: a generator with all of the nodes
        """
        if node is not None:
            yield node.value
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)

    def postorder(self, node):
        """
        same as inorder but with a postorder traversal
        :param node: the root to start with
        :return: a generator with all of the nodes
        """
        if node is not None:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node.value

    def depth(self, value):
        """
        finds the depth of the node with the given value
        :param value: value to search for
        :return: and int stating the depth of the tree at the node
        """
        depth = -1
        current = self.root
        if current is None:
            return depth
        while current is not None:

            if value == current.value:
                depth += 1
                return depth
            if self.is_leaf(current):
                return -1
            if value > current.value:
                depth += 1
                current = current.right
            if value < current.value:
                depth += 1
                current = current.left

    def height(self, node):
        """
        finds the max depth of the tree
        :param node: node to start as the root
        :return: an int stating the max depth
        """
        if node is None:
            return -1
        if node.left and node.right:
            return 1 + max(self.height(node.left), self.height(node.right))
        if node.left:
            return 1 + self.height(node.left)
        if node.right:
            return 1 + self.height(node.right)
        else:
            return 0

    def min(self, node):
        """
        finds the min value in the tree
        :param node: node to start as the root
        :return: the minimum node in the tree
        """
        if node is None:
            return None
        while node.left is not None:
            node = self.min(node.left)
        return node

    def max(self, node):
        """
        finds the max value in the tree
        :param node: node to start as the root
        :return: the maximum node in the tree
        """
        if node is None:
            return None
        while node.right is not None:
            node = self.max(node.right)
        return node

    def get_size(self):
        """
        :return: the size of the tree
        """
        return self.size

    def is_perfect(self, node):
        """
        starts at the root and checks to see if all leaf nodes are equal depth 
        and all internal nodes have 2 children
        :param node: root to start with
        :return: true if perfect, else false
        """
        if node is None:
            return True
        if node.left and node.right:
            if self.is_leaf(node.left) and self.is_leaf(node.right):
                return True
            return True and self.is_perfect(node.left) and self.is_perfect(node.right)
        else:
            return False

    def is_degenerate(self):
        """
        checks to see if all internal nodes have only 1 child
        :return: True if degenerate, else False
        """
        count = self.count(self.root)
        count -= 1
        if self.root is None:
            return False
        if count == self.height(self.root):
            return True
        else:
            return False

    def count(self, node):
        """
        counts the number of nodes in the tree
        :param node: root to start with
        :return: the number of nodes in the tree
        """
        if node is None:
            return 0
        if node.left or node.right:
            return 1 + self.count(node.left) + self.count(node.right)
        if not node.left:
            return 1
        if not node.right:
            return 1

    def is_leaf(self, node):
        """
        checks to see if the node is a leaf
        :param node: node to check
        :return: true if leaf, else false
        """
        return True if not node.left and not node.right else False
