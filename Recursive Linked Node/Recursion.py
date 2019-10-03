"""
PROJECT 2 - Recursion
Name: Chris Nastoski
PID:A53276668
"""

from Project2.LinkedNode import LinkedNode


def insert(value, node=None):
    """
    starts with the head node and recursively goes through the linked list
    until it finds the last node and adds in a new node with the new value
    :param  value: the value of the node
    :param  node: the head node if it exists
    :return: the value of the head node
    """
    if node is None or value <= node.value:
        node = LinkedNode(int(value), node)

    else:
        node.next_node = insert(value, node.next_node)  # goes on to the next node if the value is bigger than the
        # last and the node isn't None

    return node  # Since the first node is the head node and each recursive call is to the next pointer,
    #  the function will always have a final return of the head node


def string(node):
    """
    Takes in the head node and recursively adds all of the nodes to it
    :param node: The head Node
    :return: a string containing all of the nodes in the list
    """
    if node is None:
        return ""

    if node.next_node is None:
        return str(node.value)

    if node is not None:
        return str(node.value) + ", " + string(node.next_node)


def reversed_string(node):
    """
     Takes in the head node and recursively adds all of the nodes to it backwards
     :param node: The head Node
     :return: a string containing all of the nodes in the list
     """
    if node is None:
        return ""

    if node.next_node is None:
        return str(node.value)

    if node is not None:
        return reversed_string(node.next_node) + ", " + str(node.value)


def remove(value, node):
    """
    removes the first node with the given value
    :param value: the value to be removed
    :param node: the head node
    :return: the head node
    """
    if node is None:  # base case hits when there aren't any more nodes to traverse
        return None

    else:
        if node.value == value:
            return node.next_node
            # sets the next node of the node to the one after, erasing the node in between which is the node with the
            #  value to be removed
        else:
            node.next_node = remove(value, node.next_node)  # goes onto the next node to see if it is to be removed
            return node  # The stack always pops pack to the head node so that will be the final return


def remove_all(value, node):
    """
    Removes all of the nodes with value "value" in the list
    :param value: the value to look for
    :param node: the head node
    :return: the head node
    """
    if node is None:  # base case
        return None

    else:
        if node.value == value:
            return remove_all(value, node.next_node)
        else:
            node.next_node = remove_all(value, node.next_node)
            return node  # same logic  as remove


def search(value, node):
    """
    searches for the value in the list
    :param value: the value to look for
    :param node: the head node to start with
    :return: True if the value is in the list, False otherwise
    """
    if node is None:
        return False
    if value == node.value:
        return True or search(value, node.next_node)
    else:
        return False or search(value, node.next_node)


def length(node):
    """
    Calculates the number of nodes beginning with the head node
    :param node: the head node
    :return: the number of nodes
    """
    if node is None:
        return 0

    if node.next_node is None:
        return 1

    else:
        return 1 + length(node.next_node)


def sum_all(node):
    """
    Sums all of the values in the node
    :param node: the head node
    :return: the sum of all of the nodes
    """
    if node is None:
        return 0

    if node.next_node is None:
        return node.value

    else:
        return node.value + sum_all(node.next_node)


def count(value, node):
    """
    Counts the number of appearances of a value
    :param value: the number to search
    :param node: the head node
    :return: the number of times value has shown up
    """
    if node is None:
        return 0

    if (node.next_node is None) and (node.value != value):
        return 0

    elif (node.next_node is None) and (node.value == value):
        return 1

    elif node.value == value:
        return 1 + count(value, node.next_node)

    elif node.value != value:
        return 0 + count(value, node.next_node)

    else:
        return 0
