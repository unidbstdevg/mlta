from string import ascii_lowercase


class BinarySet:

    def __init__(self, size):
        self.set = [0] * size
        self.size = size

    def header(self):
        return ascii_lowercase[:self.size]

    def next(self):
        if self.set[-1] == 0:
            self.set[-1] = 1
            return True
        else:
            for i in range(self.size - 1, -1, -1):
                if self.set[i] == 0:
                    self.set[i] = 1
                    return True
                else:
                    self.set[i] = 0

        return False

    def __str__(self):
        return " ".join(map(str, self.set))

    def __iter__(self):
        for x in self.set:
            yield x
