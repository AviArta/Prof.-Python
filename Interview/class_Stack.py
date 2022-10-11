class Stack:

    def __init__(self, stack_list):
        self.stack_list = stack_list

    # проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

    # добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, element):
        self.stack_list.append(element)
        # return self.stack_list # возврат для проверки

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека.
    def pop(self, index=-1):
        if len(self.stack_list) > 0:
            self.stack_list.pop(index)  # индекс -1 используется по умолчанию.
            return self.stack_list[index]
        else:
            return self.stack_list

    # удаляет элемент стека по его значению, добавлена для использования в задаче сбалансированности скобок.
    def remove(self, element):
        self.stack_list.remove(element)

    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        if len(self.stack_list) != 0:
            return self.stack_list[-1]
        else:
            return self.stack_list

    # возвращает количество элементов в стеке.
    def size(self):
        return len(self.stack_list)


if __name__ == "__main__":
    stack_list_1 = []
    stack_list_2 = [1, 2, 3, 4, 5, 6, 7]
    stack_list_3 = ['a', 'b', 'c', 'd']

    stack_1 = Stack(stack_list=stack_list_1)
    stack_2 = Stack(stack_list=stack_list_2)
    stack_3 = Stack(stack_list=stack_list_3)

    print(stack_1.isEmpty())
    print(stack_2.isEmpty())
    print(stack_2.push(element=10))
    print(stack_2.pop())
    print(stack_2.pop())
    print(stack_2.remove(2))
    print(stack_3.peek())
    print(stack_1.size())
    print(stack_2.size())
    print(stack_3.size())

