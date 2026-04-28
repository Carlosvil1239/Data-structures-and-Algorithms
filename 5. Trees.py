# Trees and Binary Search Trees

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def print_tree(node, level=0):
    print("  " * level + str(node.value))

    for child in node.children:
        print_tree(child, level + 1)


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return BSTNode(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        return node

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is None:
            return

        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is None:
            return

        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)

    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is None:
            return

        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1

        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)

        return 1 + max(left_height, right_height)

    def find_min(self):
        if self.root is None:
            return None

        current = self.root

        while current.left is not None:
            current = current.left

        return current.value


if __name__ == "__main__":
    root = TreeNode("A")
    root.children.append(TreeNode("B"))
    root.children.append(TreeNode("C"))
    root.children[0].children.append(TreeNode("D"))

    print_tree(root)

    bst = BinarySearchTree()
    values = [8, 3, 10, 1, 6, 14, 4, 7]

    for value in values:
        bst.insert(value)

    print(bst.search(6))
    print(bst.search(99))
    print(bst.inorder())
    print(bst.preorder())
    print(bst.postorder())
    print(bst.height())
    print(bst.find_min())
