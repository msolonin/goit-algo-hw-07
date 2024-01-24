class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def sum_all_values(root):
    """ Method for sum all values in tree """
    if root is None:
        return 0
    else:
        return root.val + sum_all_values(root.left) + sum_all_values(root.right)


def min_value_node(node):
    """Method for find min value in tree"""
    current = node
    while current.left:
        current = current.left
    return current


def max_value_node(node):
    """Method for find max value in tree"""
    current = node
    while current.right:
        current = current.right
    return current


def delete(root, key):
    if not root:
        return root
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


def test_tree():
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    root = delete(root, 7)
    root = insert(root, 9)
    root = insert(root, 100)
    root = insert(root, 1)
    root = insert(root, -1)
    min_value = min_value_node(root)
    max_value = max_value_node(root)
    print(f"min value: {min_value.val}")
    print(f"max value: {max_value.val}")
    print(f"sum all values: {sum_all_values(root)}")


if __name__ == "__main__":
    test_tree()
