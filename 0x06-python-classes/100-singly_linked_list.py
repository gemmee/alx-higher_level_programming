#!/usr/bin/python3
"""This is module 100-singly_linked_list

This module contains the definition of 2 classes:
    Node and SinglyLinkedList
"""


class Node:
    """defines a node of a singly linked list

    Fields:
        data: private, must be an int
        next_node: private, must be a Node or None

    Methods:
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
        __init__(self, data, next_node=None)
    """
    def __init__(self, data, next_node=None):
        """Instantiates a Node

        Args:
            data: must be an integer, private
            next_node: must be a Node or None, optional and private
        """
        self.data = data
        self.next = next_node

    @property
    def data(self):
        """Getter for data field

        No arguments

        Returns:
            __data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data field

        Args:
            value: must be an int

        Raises:
            TypeError: If 'value' is not an integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node field

        No arguments

        Returns:
            __next attribute
        """
        return self.__next

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node attribute

        Args:
            value: must be Node or None type

        Raises:
            TypeError: If 'value' is not Node or None
        """
        if not (type(value) == Node or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next = value


class SinglyLinkedList:
    """Defines a singly linked list

    Fields:
        head: private, a Node

    Methods:
        __init__(self)
        __str__(self)
        sorted_insert(self, value)
    """
    def __init__(self):
        """Instantiates a singly linked list

        No arguments
        """
        self.__head = None

    def __str__(self):
        """String representation of a singly linked list

        No arguments
        """
        node = self.__head
        string = ""
        if node is not None:
            while node.next is not None:
                string += "{:d}\n".format(node.data)
                node = node.next
            string += "{:d}".format(node.data)
        return (string)

    def sorted_insert(self, value):
        """Insert a new value in a singly linked list by increasing value

        Args:
            value: integer value to be inserted
        """
        new = Node(value)
        node = self.__head

        if node is None:
            self.__head = new
            return

        if new.data < node.data:
            new.next = self.__head
            self.__head = new
            return

        while (node.next is not None) and (node.next.data <= new.data):
            node = node.next

        new.next = node.next
        node.next = new
        return
