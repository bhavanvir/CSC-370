# Implementation of B+-tree functionality.

from index import *

# You should implement all of the static functions declared
# in the ImplementMe class and submit this (and only this!) file.
class ImplementMe:

    # Returns a B+-tree obtained by inserting a key into a pre-existing
    # B+-tree index if the key is not already there. If it already exists,
    # the return value is equivalent to the original, input tree.
    #
    # Complexity: Guaranteed to be asymptotically linear in the height of the tree
    # Because the tree is balanced, it is also asymptotically logarithmic in the
    # number of keys that already exist in the index.
    @staticmethod
    def find(node, key):
        while not node.pointers.pointers[0] is None:
            for loc, val in enumerate(node.keys.keys):
                if val is None or val > key:
                    node = node.pointers.pointers[loc]
                    break
                elif loc == node.get_num_keys() - 1:
                    node = node.pointers.pointers[loc + 1]
                    break 
            
        return node

    @staticmethod
    def allocate_space(node, key, flag):
        tl = node.keys.keys.copy()
        tl.append(key)
        tl = sorted(tl, key = lambda x: (x is None, x))

        return (tl, Node(), tl.index(key), -(-Index.NUM_KEYS//2), 0) if flag else (tl, Node(), -(-Index.NUM_KEYS//2) - 1, 0)
            
    @staticmethod
    def parent(node, child):
        for pt in node.pointers.pointers:
            if pt is not None and pt == child: return node
        
        ck = child.keys.keys[0]

        for loc, val in enumerate(node.keys.keys):
            if val is None or val > ck: return ImplementMe.parent(node.pointers.pointers[loc], child)
        
        return ImplementMe.parent(node.pointers.pointers[Index.NUM_KEYS], child)

    @staticmethod
    def connect(nki, nn, node, child):
        nn.pointers.pointers[1] = node.pointers.pointers[2] if nki in [0, 1] else child
        nn.pointers.pointers[0] = node.pointers.pointers[1] if nki == 0 else node.pointers.pointers[2]
        if nki == 0: node.pointers.pointers[1] = child 
        node.pointers.pointers[2] = None

    @staticmethod
    def overflow(root, node, child, key):
        tl, nn, nki, si, ni = ImplementMe.allocate_space(node, key, True)
            
        for loc, val in enumerate(tl):
            if loc < si: node.keys.keys[loc] = val
            elif loc == si:
                pk = val
                node.keys.keys[loc] = None
            else:
                nn.keys.keys[ni] = val
                ni += 1
  
        ImplementMe.connect(nki, nn, node, child)

        return Node(keys = KeySet([pk, None]), pointers = PointerSet([node, nn, None])) if node == root else ImplementMe.internal(root, ImplementMe.parent(root, node), nn, pk)

    @staticmethod
    def no_overflow(root, node, child, key):
        ii = None
        for loc, val in enumerate(node.keys.keys):
            if val is None:
                node.keys.keys[loc] = key
                node.pointers.pointers[loc + 1] = child
            elif val > key: ii = loc 
        
        for i in range(Index.NUM_KEYS - 1, ii, -1): node.keys.keys[i] = node.keys.keys[i - 1]
        node.keys.keys[ii] = key
        for i in range(Index.FAN_OUT - 1, ii + 1, -1): node.pointers.pointers[i] = node.pointers.pointers[i - 1]
        node.pointers.pointers[ii + 1] = child 
        
    @staticmethod
    def internal(root, node, child, key):
        if node.keys.keys.count(None) == 0: root = ImplementMe.overflow(root, node, child, key)
        else: ImplementMe.no_overflow(root, node, child, key) 

        return root

    @staticmethod 
    def split(root, node, key):
        tl, nn, si, ni = ImplementMe.allocate_space(node, key, False)

        for loc, val in enumerate(tl):
            if loc <= si: node.keys.keys[loc] = val
            else:
                nn.keys.keys[ni] = val
                if loc < Index.NUM_KEYS: node.keys.keys[loc] = None 
                ni += 1
        
        nn.pointers.pointers[Index.FAN_OUT - 1] = node.pointers.pointers[Index.FAN_OUT - 1]
        node.pointers.pointers[Index.FAN_OUT - 1] = nn
        
        return Node(keys = KeySet([nn.keys.keys[0], None]), pointers = PointerSet([node, nn, None])) if node == root else ImplementMe.internal(root, ImplementMe.parent(root, node), nn, nn.keys.keys[0])

    @staticmethod
    def InsertIntoIndex(index, key):
        if ImplementMe.LookupKeyInIndex(index, key): return index 
        
        curr = ImplementMe.find(index.root, key)
        if curr.keys.keys.count(None) == 0: return Index(ImplementMe.split(index.root, curr, key)) 
        
        for loc, val in enumerate(curr.keys.keys):
            if val is None:
                curr.keys.keys[loc] = key
                break
        curr.keys.keys = sorted(curr.keys.keys, key = lambda x: (x is None, x))
        
        return index

    # Returns a boolean that indicates whether a given key
    # is found among the leaves of a B+-tree index.
    #
    # Complexity: Guaranteed not to touch more nodes than the
    # height of the tree
    @staticmethod
    def LookupKeyInIndex(index, key):
        return (ImplementMe.find(index.root, key)).keys.keys.count(key) != 0

    # Returns a list of keys in a B+-tree index within the half-open
    # interval [lower_bound, upper_bound)
    #
    # Complexity: Guaranteed not to touch more nodes than the height
    # of the tree and the number of leaves overlapping the interval.
    @staticmethod
    def RangeSearchInIndex(index, lower_bound, upper_bound):
        curr, head = ImplementMe.find(index.root, lower_bound), None

        if lower_bound == upper_bound and ImplementMe.LookupKeyInIndex(index, lower_bound): return [lower_bound]
        
        for loc, val in enumerate(curr.keys.keys):
            if val >= lower_bound:
                head = loc
                break
    
        if head is None or curr.keys.keys[head] >= upper_bound: return []
        vl = [curr.keys.keys[head]]

        while not val >= upper_bound:
            if head == 0:
                if curr.keys.keys[1] is None: curr.keys.keys[1] = curr.keys.keys[0]
                elif curr.keys.keys[1] < upper_bound: vl.append(curr.keys.keys[1])
                head += 1
            else:
                curr = curr.pointers.pointers[2]
                if curr is None: return vl 
                elif curr.keys.keys[0] < upper_bound: vl.append(curr.keys.keys[0])
                head = 0
        
        return list(filter(None, vl))
