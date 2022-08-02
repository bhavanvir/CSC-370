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
    def is_leaf(node):
        return node.pointers.pointers[0] is None

    @staticmethod
    def find(root, key):
        curr = root
        while not ImplementMe.is_leaf(curr):
            for loc, val in enumerate(curr.keys.keys):
                if val is None or val > key:
                    curr = curr.pointers.pointers[loc]
                    break
                elif loc == curr.get_num_keys() - 1:
                    curr = curr.pointers.pointers[loc + 1]
                    break 
        
        return curr

    @staticmethod
    def InsertIntoIndex(index, key):
        return index

    # Returns a boolean that indicates whether a given key
    # is found among the leaves of a B+-tree index.
    #
    # Complexity: Guaranteed not to touch more nodes than the
    # height of the tree
    @staticmethod
    def LookupKeyInIndex(index, key):
        curr = ImplementMe.find(index.root, key)

        return curr.keys.keys.count(key) != 0

    # Returns a list of keys in a B+-tree index within the half-open
    # interval [lower_bound, upper_bound)
    #
    # Complexity: Guaranteed not to touch more nodes than the height
    # of the tree and the number of leaves overlapping the interval.
    @staticmethod
    def RangeSearchInIndex(index, lower_bound, upper_bound):
        curr = ImplementMe.find(index.root, lower_bound)
        head = None

        if lower_bound == upper_bound and ImplementMe.LookupKeyInIndex(index, lower_bound):
            return [lower_bound]
        
        for loc, val in enumerate(curr.keys.keys):
            if val >= lower_bound:
                head = loc
                break
    
        if head is None or curr.keys.keys[head] >= upper_bound:
            return []
        vl = [curr.keys.keys[head]]

        while not val >= upper_bound:
            if head == 0:
                val = curr.keys.keys[1]
                if val is None:
                    val = curr.keys.keys[0]
                elif val < upper_bound:
                    vl.append(val)
                head += 1
            elif head != 0:
                curr = curr.pointers.pointers[2]
                if curr is None:
                    return vl 
                elif curr.keys.keys[0] < upper_bound:
                    vl.append(curr.keys.keys[0])
                head = 0
        
        return list(filter(None, vl))
