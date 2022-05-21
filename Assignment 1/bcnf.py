# Counts the number of steps required to decompose a relation into BCNF.

from relation import *
from functional_dependency import *

# You should implement the static function declared
# in the ImplementMe class and submit this (and only this!) file.
# You are welcome to add supporting classes and methods in this file.
class ImplementMe:
    # Returns the number of recursive steps required for BCNF decomposition
    #
    # The input is a set of relations and a set of functional dependencies.
    # The relations have *already* been decomposed.
    # This function determines how many recursive steps were required for that
    # decomposition or -1 if the relations are not a correct decomposition.
    @staticmethod
    def DecompositionSteps(relations, fds):
        fdep = fds.functional_dependencies
        fset = [[] for i in range(len(fdep))]
        lhs = set()
        rhs = set()

        i = 0
        for fd in fdep:
            lhs.update(fd.left_hand_side)
            rhs.update(fd.right_hand_side)
            attributes = fd.left_hand_side.union(fd.right_hand_side)
            if i < len(fdep):
                fset[i] = Helpers.closure(fds, attributes)
                i += 1
        
        violations = Helpers.violations(relations, fset)
        violations = [i for i in violations if i]
        #print(Helpers.isimplied(fds, lhs, rhs))

        return 500

class Helpers:
    @staticmethod
    def closure(fds, attributes):
        fdep = fds.functional_dependencies
        result = set(attributes)
        more = True
        while more:
            more = False
            for fd in fdep:
                if fd.left_hand_side.issubset(result) and not fd.right_hand_side.issubset(result):
                    result.update(fd.right_hand_side)
                    more = True

        return result

    @staticmethod
    def violations(relations, fset):
        rels = relations.relations
        relation = set()
        for r in rels:
            relation.update(r.attributes)
        
        violations = [[] for i in range(len(fset))]
        for i in range(len(fset)):
            if relation.difference(fset[i]) != set():
                violations[i] = fset[i]

        return violations

    @staticmethod
    def project(fds, attributes):
        fdep = fds.functional_dependencies
        result = set()
        for fd in fdep:
            if fd.left_hand_side.issubset(attributes) and fd.right_hand_side.issubset(attributes):
                result.add(fd)
        return result
    
    @staticmethod 
    def isimplied(fds, lhs, rhs):
        return Helpers.closure(fds, lhs).issuperset(rhs)
