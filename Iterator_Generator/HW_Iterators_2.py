nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]]


class FlatIterator:

    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.cursor = - 1
        return self

    def do_linear_list(self, list_):
        linear_list = []
        for element in list_:
            if type(element) != list:
                linear_list.append(element)
            else:
                for i in self.do_linear_list(element):
                    linear_list.append(i)
        return linear_list

    def __next__(self):
        linear_list = self.do_linear_list(self.list_)
        self.cursor += 1
        if self.cursor > len(linear_list):
            raise StopIteration
        else:
            if self.cursor == len(linear_list):
                raise StopIteration
            return linear_list[self.cursor]

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    print()
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)


# Рабочая функция распаковки списков любой вложенности в один.
# def do_linear_list(list_):
#     linear_list = []
#     for element in list_:
#         if type(element) != list:
#             linear_list.append(element)
#         else:
#             for i in do_linear_list(element):
#                 linear_list.append(i)
#     return linear_list
#
# print(do_linear_list(nested_list))