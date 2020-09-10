"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):

        if self.value == target:
            return True

        if self.value != target:

            if self.value < target:
                if self.right is None:
                    return False
                return self.right.contains(target)
            elif self.value > target:
                if self.left is None:
                    return False
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        current_node = self

        while current_node is not None:
            print(current_node.value)
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.right

        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        """
        Recursive 
        1, call on the current node value
        2, check if there's a left side
            i. move down the left side using for each
        3, check if there's a right side
            i. move down the right side using for each
        """
        fn(self.value)  # step 1, call on current node value
        if self.left is not None:
            self.left.for_each(fn)  # step 2 & 2i
        if self.right is not None:
            self.right.for_each(fn)  # step 3 & 3i

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        """
        1, find the node you're on
            1i. check if left side
        2, go down left side first and print it (using RECURSION)
        3, root node gets printed before going down the right side
            3i. check if there is a right side
        4, go down right side and print it (using RECURSION)
        """
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)  # printing in the middle
        if self.right is not None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()
