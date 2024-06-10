class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.start < self.end:
            if self.i % 2:
                return self.i
        raise StopIteration()


en = EvenNumbers(10, 25)
for i in en:
    print(i)
