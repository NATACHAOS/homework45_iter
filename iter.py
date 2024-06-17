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
            print('\n'.join(map(str, range((self.start + self.start % 2), (self.end + 1), 2))))
        raise StopIteration()


en = EvenNumbers(10, 25)
for i in en:
    print(i)
