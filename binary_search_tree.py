class BSDNode(object):
	"""docstring for ClassName"""
	def __init__(self, key, value, left=None, right=None):
		self.key = key
		self.value = key
		self.left = left
		self.right = right
		
class BST(object):
    def __init__(self, root):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_node_dict = {}
        for node_dict in node_list:
            key = node_dict['key']
            key_to_node_dict[key] = BSDNode(key, value=key)
        for node_dict in node_list:
        	key = node_dict['key']
        	node = key_to_node_dict['key']
        	if node_dict['is_root']:
        		root = node
        	node.left = key_to_node_dict.get(node_dict['left'])
        	node.right = key_to_node_dict.get(node_dict['right'])
        	cls.size += 1
        return cls(root)
    def _bst_search(self, subtree, key):
    	if subtree is None:
    		return None
    	elif subtree.key > key:
    		return self._bst_search(subtree.left)
    	elif subtree.key < key:
    		return self._bst_search(subtree.right)
    	else:
    		return subtree
    def get(self, key, default=None):
    	node = self._bst_search(self.root, key)
    	if node is None:
    		return None
    	else:
    		return node.value

    def _bst_min_node(self, subtree):
    	if subtree is None:
    		return None
    	elif subtree.left is None:
    		return subtree
    	else:
    		self._bst_min_node(subtree.left)

    def bst_min(self):
    	node = _bst_min_node(self.root)
    	return node.value if node else None

    def _bst_insert(self, subtree, key, value):
    	if subtree is None:
    		subtree = BSDNode(key, value)
    	elif key < subtree.key:
    		subtree.left = self._bst_insert(subtree.left, key, value)
    	elif key > subtree.key:
    		subtree.right = self._bst_insert(subtree.right,key, value)
    	return subtree
    def add(self, key, value):
    	node = _bst_search(self.root, key)
    	if node is not None:
    		node.value = value
    		return False
    	else:
    		self.root = self._bst_insert(self.root, key, value)
    		self.size += 1
    		return True

    def _bst_remove(self, subtree, key):
    	if subtree is None:
    		return None
    	elif key < subtree.key:
    		subtree.left = self._bst_remove(subtree.left,key)
    		return subtree
    	elif key > subtree.key:
    		subtree.right = self._bst_remove(subtree.right, key)
    		return subtree
    	else:
    		if subtree.left is None and subtree.right is None:
    			return None
    		elif subtree.left is None or subtree.right is None:
    			if subtree.left is not None:
    				return subtree.left
    			else:
    				return subtree.right
    		else:
    			successor_node = self._bst_min_node(subtree.right)
    			subtree.key, subtree.value = successor_node.key, successor_node.value
    			subtree.right = self._bst_remove(subtree.right,successor_node.key)
    			return successor



