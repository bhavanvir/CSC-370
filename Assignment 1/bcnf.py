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
    def DecompositionSteps( relations, fds ):
        dependency_set = fds.functional_dependencies
        lhs, rhs = [], []
        for functional_dependency in dependency_set:
            lhs.append(functional_dependency.left_hand_side)
            rhs.append(functional_dependency.right_hand_side)

        relation_set = relations.relations
        relations = []
        for relation in relation_set:
            relations.extend(relation.attributes)
        relations = set(relations)

        combined = [[] for i in range(len(lhs))]
        for i in range(len(lhs)):
            combined[i].extend(lhs[i])
            combined[i].extend(rhs[i])

        """
        Compute the intersection between all pairs of items in the combined list,
        then union the intersection set with the appropriate FD
        """
        difference = []
        for i in range(len(combined)):
            if i + 1 < len(combined):
                difference.append(set(combined[i]).intersection(combined[i + 1]))
        print(combined, "AND", difference)
                
        closure_diff = [[] for i in range(len(lhs))]
        for i in range(len(lhs)):
            closure_diff[i] = (relations.difference(combined[i])).union(lhs[i])

        return 500
