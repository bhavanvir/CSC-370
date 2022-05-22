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
        lhs = set()
        rhs = set()

        i = 0
        for fd in fdep:
            lhs.update(fd.left_hand_side)
            rhs.update(fd.right_hand_side)
        
        Helpers.decompose(relations, fds)
    
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
    def violations(relations, fds):
        fdep = fds.functional_dependencies
        fset = [[] for i in range(len(fdep))]

        i = 0
        for fd in fdep:
            attributes = fd.left_hand_side.union(fd.right_hand_side)
            if i < len(fdep):
                fset[i] = Helpers.closure(fds, attributes)
                i += 1

        rels = relations.relations
        relation = set()
        for r in rels:
            relation.update(r.attributes)
        
        violations = [[] for i in range(len(fset))]
        for i in range(len(fset)):
            if relation.difference(fset[i]) != set():
                violations[i] = fset[i]

        lhs = [FunctionalDependency for i in range(len(violations))]
        i = 0
        for fd, v in zip(fdep, violations):
            if v:
                lhs[i] = fd
                i += 1
        lhs = [i for i in lhs if i is not FunctionalDependency]
        
        return lhs

    @staticmethod 
    def isimplied(fds, lhs, rhs):
        return Helpers.closure(fds, lhs).issuperset(rhs)

    @staticmethod
    def minimize(fds, lhs, rhs):
        cand = lhs.copy()
        for l, r in zip(lhs, rhs):
            cand.remove(l)
            if not Helpers.isimplied(fds, l, r):
                cand.extend(l)
        return cand

    @staticmethod
    def project(fds, attributes):
        fdep = fds.functional_dependencies
        lhs, rhs = [], []
        result = set()
        for fd in fdep:
            if fd.left_hand_side.issubset(attributes) and fd.right_hand_side.issubset(attributes):
                lhs.append(fd.left_hand_side)
                rhs.append(fd.right_hand_side)
                result.add(fd)
        print(result)
        #return Helpers.minimize(fds, lhs, rhs)
    
    @staticmethod
    def decompose(relations, fds):
        decompositions = []

        rels = relations.relations
        rset = set()
        for r in rels:
            rset.update(r.attributes)

        violations = Helpers.violations(relations, fds)
        if len(violations) == 0:
           return rset
        else:
            for v in violations:
                c = Helpers.closure(fds, v.left_hand_side.union(v.right_hand_side))
                R1 = c
                R2 = (rset.difference(c)).union(v.left_hand_side)
            print(R1, "AND", R2)
