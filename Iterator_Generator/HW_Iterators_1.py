nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]]

class FlatIterator:

    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.cursor = 0
        self.cursor2 = - 1
        return self

    def __next__(self):
        if self.cursor2 > len(self.list_[self.cursor]) - 1:
            raise StopIteration
        else:
            if self.cursor2 < len(self.list_[self.cursor]) - 1:
                self.cursor = self.cursor
                self.cursor2 += 1
                return self.list_[self.cursor][self.cursor2]
            elif self.cursor2 == len(self.list_[self.cursor]) - 1:
                self.cursor += 1
                self.cursor2 = 0
            if self.cursor > len(self.list_) - 1:
                raise StopIteration
            else:
                if self.cursor <= len(self.list_) - 1:
                    self.cursor = self.cursor
                    self.cursor2 = 0
                    return self.list_[self.cursor][self.cursor2]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    print()

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)