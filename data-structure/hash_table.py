"""Hash Table."""


class HashTable(object):
    """Hash Table.
    """

    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):

        indx = self.calculate_hash_value(string)
        if self.table[indx]:
            self.table[indx].append(string)
        else:
            self.table[indx] = [string]

    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        try:
            if string in self.table[hash_value]:
                return hash_value
            else:
                return -1
        except:
            return -1

    def calculate_hash_value(self, string):

        hash_value = ord(string[0]) * 100 + ord(string[1])
        return hash_value


if __name__ == "__main__":

    hash_table = HashTable()

    # Should be 8568
    print(hash_table.calculate_hash_value('UDACITY'))

    # Should be -1
    print(hash_table.lookup('UDACITY'))

    hash_table.store('UDACITY')
    # Should be 8568
    print(hash_table.lookup('UDACITY'))

    hash_table.store('UDACIOUS')
    # Should be 8568
    print(hash_table.lookup('UDACIOUS'))
