class UF:
    """An implementation of union find data structure.
    It uses weighted quick union by rank with path compression.
    """

    def __init__(self, number_of_items):
        """Initialize an empty union find object with N items.

        Args:
            N: Number of items in the union find object.
        """
        #number_of_items = 5
        self._id = list(range(number_of_items)) #[0, 1, 2, 3, 4]
        self._rank = [0] * number_of_items #[0, 0, 0, 0, 0]

    def find(self, p):
        """Find the set identifier for the item p."""

        id = self._id
        while p != id[p]:
            p = id[p] = id[id[p]]   # Path compression using halving.
        return p

    def connected(self, p, q):
        """Check if the items p and q are on the same set or not."""

        return self.find(p) == self.find(q)

    def union(self, p, q):
        """Combine sets containing p and q into a single set."""

        id = self._id
        rank = self._rank

        i = self.find(p)
        j = self.find(q)
        if i == j:
            self.print_method(('ij: ', j))
            self.print_method(('id[j]: ', id[j]))
            self.print_method(('rank[j]: ', rank[j]))
            return

        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

    def __str__(self):
        """String representation of the union find object."""
        return " ".join([str(x) for x in self._id])

    def __repr__(self):
        """Representation of the union find object."""
        return "UF(" + str(self) + ")"
    
    def print_method(self, msg):
        print(msg, flush=True) 

