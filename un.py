class UN:
    """an simpler implementation of quick union find not using path compression/halvation"""

    def __init__(self, number_of_items):
        self.id = []
        for item in range(len((number_of_items))):
            self.id.append(item)
        self.print_method(('self.id: ', self.id))

    def find(self, j):
        #self.print_method(('j: ', j, ' self.id[j]', self.id[j]))
        while j != self.id[j]:
            self.print_method('j != self.id[j]')
            j = self.id[j]
            self.print_method(('j: ', j, ' self.id[j]', self.id[j]))
        #self.print_method(('returning j: ', j))
        return j
    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            self.print_method(('i: ', i))
            self.print_method(('id: ', self.id[j]))
            return

    def print_method(self, msg):
        print(msg, flush=True)

    def __str__(self):
        """String representation of the union find object."""
        return " ".join([str(x) for x in self.id])

    def __repr__(self):
        """Representation of the union find object."""
        return "UF(" + str(self) + ")"
