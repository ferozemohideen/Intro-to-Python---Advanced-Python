class BinaryTree:
    """
    This class is a binary tree implementation.

    Don't modify class or method names, just implement methods that currently raise
    a NotImplementedError!
    """

    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add(self, node):
        # The root is None, so set the root to be the new Node.
        if not self.__root:
            self.__root = node
        else:
            # Start iterating over the tree.
            marker = self.__root
            while marker:
                if node.value == marker.value:
                    # Raise a ValueError, because the node's value already exists.
                    raise ValueError("Value already exists!")
                elif node.value > marker.value:
                    # Move to the right in the tree.
                    if not marker.get_right():
                        marker.set_right(node)
                        return
                    marker = marker.get_right()
                else:
                    # Move to the left in the tree.
                    if not marker.get_left():
                        marker.set_left(node)
                        return
                    marker = marker.get_left()

    def find(self, value):
        marker = self.__root

        while marker:
            if marker.value == value:
                return marker
            elif value > marker.value:
                marker = marker.get_right()
            else:
                marker = marker.get_left()
        raise LookupError("couldn't find value")


    def print_inorder(self):
        self.__print_inorder_r(self.__root)

    def __print_inorder_r(self, current_node):
        if not current_node:
            return
        self.__print_inorder_r(current_node.get_left())
        print(current_node.print_details())
        self.__print_inorder_r(current_node.get_right())


        15
   11      20
10    13    17
7     12   14