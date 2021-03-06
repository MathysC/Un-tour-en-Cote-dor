from Algorithmes.GreedyAlgorithms.Greedy import Greedy
from Geography.Town import Town
from Rounds.NormalRound import NormalRound


class GreedyNI(Greedy):
    """
    Class GreedyNI extends Greedy for the Nearest Insertion Greedy Algorithm
    """

    def __init__(self, towns):
        """
        Constructor of GreedyNI

        :param towns: the list of towns
        :type towns: list
        """
        super().__init__(towns, "gloutonne \"insertion proche\"")

    def greedyMethod(self) -> NormalRound:
        """
        Calculate the round from the two further towns with closer towns



        :return: A Round made of nearest Neighbor from the two further starting towns
        :rtype: Round

        .. seealso:: starting_Further_Towns(self)
        """
        record = {}
        # Get the two most distant towns
        v1, v2 = self.starting_Further_Towns()
        # add both to the visited list and the round list
        R2 = [v1, v2]
        self.visited = [v1, v2]
        # While all town aren't visited
        while len(set(self.listTown).difference(self.visited)) > 0:
            # clear the record
            record.clear()
            # for each town unvisited
            for town in set(self.listTown).difference(self.visited):
                # get the distance from all town already visited
                for i in range(0, len(R2)):
                    # calculate the distance between the town and others around it
                    dist = R2[i].distance(town) + \
                           town.distance(R2[(i + 1) % len(R2)]) - \
                           R2[i].distance(R2[(i + 1) % len(R2)])
                    # register the information
                    record[dist] = [town, i]

            # get the best town and iterator from the best distance value
            best = record.get(min(record))
            # Insert at the ite + 1 % len(R2) the best town :
            # It insert at the beginning when the ite is the last one of R2
            R2.insert((best[1]+1) % len(R2), best[0])
            self.visited.append(best[0])

        return NormalRound(R2, "insertion proche")
