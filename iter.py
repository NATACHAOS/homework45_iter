class EvenNumbers:
    """Перебор чётных чисел в определённом числовом диапазоне"""
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.start = self.start
        self.result = self.start
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration()
        elif self.start % 2 == 0:
            self.result = self.start
            self.start += 1
            return self.result
        else:
            self.start += 1


en = EvenNumbers(10, 25)
for i in en:
    if i != None:
        print(i)