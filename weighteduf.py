class WUF:
    """ simple attempted implementation of a weighted union"""
    
    def __init__(self, number_of_items):
        """
        Args:
            N: Number of items in the weighted union 
        """
        self.i_index = list(range(number_of_items))
        self.j_index = []
        for _ in range(number_of_items):
            self.j_index.append(1)
    
    def root(self, index):
        while index != self.i_index[index]:
            index = self.i_index[index]
        return index

    def union(self, p, q):
        index_i = self.root(p)
        index_j = self.root(q)
        if self.j_index[index_i] < self.j_index[index_j]:
            self.i_index[index_i] = index_j
            self.j_index[index_j] += self.j_index[index_i]
        else:
            self.i_index[index_j] = index_i
            self.j_index[index_i] = self.j_index[index_j]

    def __str__(self):
        """String representation of the union find object."""
        str1 = " ".join([str(x) for x in self.i_index])
        str1 += " ".join([str(x) for x in self.j_index])
        return str1

    def __repr__(self):
        """Representation of the union find object."""
        return "UF(" + str(self) + ")"

    def print_method(self, msg):
        print(msg, flush=True)
