from random import randint

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.l = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        i = self.d[val]
        self.d[self.l[-1]] = i
        self.d.pop(val)
        self.l[i], self.l[len(self.l) - 1] = self.l[len(self.l) - 1], self.l[i]
        self.l.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.l[randint(0, len(self.l) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
