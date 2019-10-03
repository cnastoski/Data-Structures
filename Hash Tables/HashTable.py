class HashNode:
    """
    DO NOT EDIT
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return "HashNode({self.key}, {self.value})"


class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        pass

    def __str__(self):
        """
        method to help debug. calls the print statement to print out the hash table
        :return: the string form of the hash table
        """
        final = ""
        for node in self.table:
            if node is not None:
                if node is not False:
                    final += "[" + node.key + ", " + str(node.value) + "]" + ", "

        return final[0:-2]

    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity

    def insert(self, key, value):
        """
        inserts a HashNode into the table if the key is not empty, updates the value if the key is the same. calls grow
        if the load factor is greater than 0.75
        :param key: the key of the node
        :param value: the value of the node
        :return:
        """
        if value is "" or key is "":
            return -1
        data = HashNode(key, value)
        index = self.quadratic_probe(key)
        if self.table[index] is None or self.table[index] is False:
            self.table[index] = data
            self.size += 1

        else:
            self.table[index].value = value

        if (self.size / self.capacity) > 0.75:
            self.grow()

    def quadratic_probe(self, key):
        """
        method to resolve conflicts with hashing.
        :param key: the key to search for
        :return: the index where the key is if it exists, the next available spot if not
        """
        if key == "" or key is None:
            return -1
        i = 0
        bucket = (self.hash_function(key) + i * i) % self.capacity
        while self.table[bucket] is not None:
            if not self.table[bucket]:
                return bucket

            elif self.table[bucket].key == key:
                return bucket

            else:
                bucket = (bucket + (i + 1) * (i + 1)) % self.capacity

        return bucket

    def find(self, key):
        """
        finds the node with the key
        :param key: the key to search for
        :return: the node with the key if found, False if not
        """
        i = 0
        bucket = (self.hash_function(key) + i * i) % self.capacity
        while self.table[bucket] is not None:
            if self.table[bucket].key == key:
                return self.table[bucket]

            else:
                bucket = (bucket + (i + 1) * (i + 1)) % self.capacity

        return False

    def lookup(self, key):
        """
        finds the value of the node with the given key
        :param key: the key to search for
        :return: the value of the node with the given key, False if node not found
        """
        found = self.find(key)
        if found:
            return found.value
        return False

    def delete(self, key):
        """
        Takes in a key to delete in the Hash Table. Deletes the node by setting the index to False
        :param key: the key to delete
        :return: Nothing
        """
        i = 0
        bucket = (self.hash_function(key) + i * i) % self.capacity
        while self.table[bucket] is not None:
            if self.table[bucket] is not False:
                if self.table[bucket].key == key:
                    self.table[bucket] = False
                    self.size -= 1

            bucket = (bucket + (i + 1) * (i + 1)) % self.capacity

    def grow(self):
        """
        doubles the capacity and rehashes all items in the table
        :return: Nothing
        """
        self.capacity *= 2
        aux = self.rehash()
        self.table = aux

    def rehash(self):
        """
        rehashes all items in the table
        :return: the rehashed table
        """
        auxiliary = self.table
        self.table = [None] * self.capacity
        for pair in auxiliary:
            if pair is not None:
                index = self.quadratic_probe(pair.key)
                if self.table[index] is None:
                    self.table[index] = pair
                else:
                    self.table[index].value = pair.value

        return self.table


def string_difference(string1, string2):
    """
    Takes in two strings and returns the difference of the characters
    :param string1: one string to compare
    :param string2: the other string to compare
    :return: a set containing the differing characters
    """
    if string1 == string2:
        return set()
    size = 4
    while ((len(string1) + len(string2)) / size) > 0.75:  # assumes worst case space consumption
        size *= 2
    hasht = HashTable(size)
    for char in string1:
        data = HashNode(char, 1)
        index = hasht.quadratic_probe(char)
        if hasht.table[index] is None:
            hasht.table[index] = data
            hasht.size += 1

        else:
            hasht.table[index].value += 1

    for char in string2:
        data = HashNode(char, -1)
        index = hasht.quadratic_probe(char)
        if hasht.table[index] is None:
            hasht.table[index] = data
            hasht.size += 1

        elif hasht.table[index].key == char:
            hasht.table[index].value -= 1

        else:
            hasht.table[index].value -= 1

    difference = set()
    for node in hasht.table:
        if node is not None:
            if node.value is not 0:
                difference.add(node.key * abs(node.value))
    return difference
