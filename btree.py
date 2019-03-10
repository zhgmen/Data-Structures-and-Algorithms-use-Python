from collections import deque

class Queue(object):
    def __init__(self):
        self._items = deque()
        
    def append(self,value):
        return self._items.append(value)
    def pop(self):
        return self._items.popleft()
    def empty(self):
        return len(self._items) == 0

class Stack(object):
    def __init__(self):
        self._items = deque()
    def push(self, value):
        return self._items.append(value)
    def pop(self):
        return self._items.pop()
    def empty(self):
        return len(self._items)==0

class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinTree(object):
    def __init__(self, root=None):
        self.root = root
    @classmethod
    def build_from(cls, node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)
    def preorder_trav(self,subtree):
        if subtree is not None:
            print subtree.data
            preorder_trav(subtree.left)
            preorder_trav(subtree.right)
    def preorder_trav_use_stack(self, subtree):
        s = Stack()
        if subtree:
            s.push(subtree)
            while not s.empty():
                top_node = s.pop()
                print top_node
                if top_node.right:
                    s.push(top_node.right)
                if top_node.left:
                    s.push(top_node.left)
    def inorder_trav(self, subtree):
        if subtree is not None:
            self.inorder_trav(subtree.left)
            print subtree.data
            self.inorder_trav(subtree.right)
    def yield_inorder(self, subtree):
        if subtree:
            yield from self.inorder(subtree.left)
            yield subtree.val
            yield from self.inorder(subtree.right)
    def reverse(self, subtree):
        if subtree:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)
    def layer_trav(self, subtree):
        cur_nodes = [subtree]
        next_nodes = []
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                print node.data
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_nodes = next_nodes
            next_nodes = []

    def layer_trav_use_queue(self, subtree):
        q = Queue()
        q.append(subtree)
        while not q.empty():
            cur_node = q.pop()
            print cur_node.data
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
                
            
            
            
            
        
        
