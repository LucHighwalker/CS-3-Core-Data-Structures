from hashtable import HashTable


class Set(object):

    def __init__(self, elements=None):
        self.table = HashTable()

        if elements is not None:
            for element in elements:
                self.table.set(element, None)

    def __str__(self):
        items = ['{!r}'.format(element) for element in self]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        return 'Set({!r})'.format(self.table.keys())

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.table.size

    def __iter__(self):
        elements = self.table.keys()
        for element in elements:
            yield element

    def add(self, element):
        self.table.set(element, None)

    def remove(self, element):
        self.table.delete(element)

    def contains(self, element):
        return self.table.contains(element)

    def union(self, set):
        new_set = Set(self)
        for element in set:
            new_set.add(element)
        return new_set
