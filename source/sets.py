from hashtable import HashTable


class Set(object):

    def __init__(self, elements=None):
        self.table = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        items = ['{!r}'.format(element) for element in self]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        return 'Set({!r})'.format(self.table.keys())

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        elements = self.table.keys()
        for element in elements:
            yield element

    def add(self, element):
        self.table.set(element, None)
        self.size = self.table.length()

    def remove(self, element):
        self.table.delete(element)
        self.size = self.table.length()

    def contains(self, element):
        return self.table.contains(element)

    def union(self, set):
        new_set = Set(self)
        for element in set:
            new_set.add(element)
        return new_set

    def difference(self, other):
        diff = Set()
        for element in other:
            if element not in self:
                diff.add(element)
        return diff

    def is_subset(self, other):
        if len(self) > len(other):
            return False
        else:
            for element in self:
                if element not in other:
                    return False
            return True

    def intersection(self, other):
        intersect = Set()
        if len(self) > other:
            for element in other:
                if element in self:
                    intersect.add(element)
        else:
            for element in self:
                if element in other:
                    intersect.add(element)
        return intersect


# def main():
#     st = Set(['A', 'B', 'C'])
#     print(st)
#     print('size: {}'.format(st.size))

# if __name__ == '__main__':
#     main()
