#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        nw_nd = Node(value)
        if self.__head is None:
            nw_nd.next_node = None
            self.__head = nw_nd
        elif self.__head.data > value:
            nw_nd.next_node = self.__head
            self.__head = nw_nd
        else:
            cp = self.__head
            while (cp.next_node is not None and
                    cp.next_node.data < value):
                cp = cp.next_node
            nw_nd.next_node = cp.next_node
            cp.next_node = nw_nd

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        cp = self.__head
        while cp is not None:
            values.append(str(cp.data))
            cp = cp.next_node
        return ('\n'.join(values))
