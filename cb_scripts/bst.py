#!/usr/bin/env python3

"""Binary Search Tree."""


class Node:
    """Node for Binary Tree."""

    def __init__(self, value, left=None, right=None, root=True):
        """Node for Binary Search Tree.

        value - Value to be stored in the tree node.
        left node - default value is None.
        right node - default value is None.
        root - default value is True.
        """
        self.value = value
        self.left = left
        self.right = right
        self.root = root

    def insert(self, value):
        """Insert new value into BST."""
        if self.value:
            # Determine left or right insertion
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, root=False)
                else:
                    self.left.insert(value)
            if value > self.value:
                if self.right is None:
                    self.right = Node(value, root=False)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def find(self, value):
        """Find value in BST."""
        if value < self.value:
            if self.left is None:
                return "Not found."
            return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return "Not found."
            return self.right.find(value)
        else:
            print(self.value, "Found")

    def print_tree(self):
        """Print the BST."""
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()


if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.print_tree()
