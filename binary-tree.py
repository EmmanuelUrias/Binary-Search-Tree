class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:  # if there is a duplicate value stop, this is because in a binary tree there is no duplicates allowed
            return

        elif data < self.data:
            if self.left:  # add data to left subtree
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:  # add data to left subtree
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:  # visit left tree
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        # base node
        elements.append(self.data)

        if self.left:  # visit left tree
            elements += self.left.in_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:  # visit left tree
            elements += self.left.in_order_traversal()

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        # base node
        elements.append(self.data)

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            self.left.find_min()

    def insert(self, val):
        if val == self.data:
            return
        elif val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinarySearchTreeNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinarySearchTreeNode(val)

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.left.find_min()
            self.data = min_val
            self.left = self.left.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    numbers_tree.insert(19)
    print(numbers_tree.in_order_traversal())
