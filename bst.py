class Node:
    def __init__(self, key, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.key = key
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root:
            self._insert(key, self.root)
        else:
            self.root = Node(key)

    def _insert(self, key, node):
        if key < node.key:
            if node.left:
                self._insert(key, node.left)
            else:
                node.left = Node(key, parent=node)
        else:
            if node.right:
                self._insert(key, node.right)
            else:
                node.right = Node(key, parent=node)

    def print_root(self):
        print("root is ", end='')
        print(self.root.key)

    def get_node(self, key, node):
        if key == node.key:
            return node
        elif key < node.key:
            return self.get_node(key, node.left)
        else:
            return self.get_node(key, node.right)

    def remove(self, key):
        self._remove(self.get_node(key, self.root))

    
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v != None:
            v.parent = u.parent

    def get_min(self, root):
        x = root
        while x.left != None:
            x = x.left
        return x

    
    def _remove(self, z):
        tosplay = None
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.get_min(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0

        lheight = self._height(node.left)
        rheight = self._height(node.right)
        return max(lheight, rheight) + 1

    def search(self, key):
        return self._search(key, self.root)

    def _search(self, key, node):
        if not node:
            print("NOT PRESENT!!!")
        elif key == node.key:
            print("PRESENT")
            print(node.key)
        elif key < node.key:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)

    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)
