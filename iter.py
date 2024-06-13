class EvenNumbers:
    def __init__(self, start, end):
        self.start = 0
        self.end = 1
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.start < self.end:
            for num in range(self.start, self.end):
                if num % 2 == 0:
                    return num
        raise StopIteration()


en = EvenNumbers(10, 25)
for i in en:
    print(i)
