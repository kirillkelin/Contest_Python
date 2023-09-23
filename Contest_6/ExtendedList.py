import sys


class ExtendedList(list):
    @property
    def reversed(self):
        return list(reversed(self))

    R = reversed

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, value):
        self[0] = value

    F = first

    @property
    def last(self):
        return self[len(self) - 1]

    @last.setter
    def last(self, value):
        self[len(self) - 1] = value

    L = last

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, value):
        if len(self) > value:
            self[:] = self[:value]
        else:
            for i in range(value - len(self)):
                self.append(None)

    S = size


exec(sys.stdin.read())

