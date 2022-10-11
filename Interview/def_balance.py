from class_Stack import Stack


def check_balance(text):
    ''' Функция решает задачу на проверку сбалансированности скобок, используя функции класса Stack:
    isEmpty, size, push, remove.
    '''
    text_list = list(text)
    text_list_copy = text_list.copy()
    help_list = []
    if Stack(text_list).size() % 2 == 0:
        for element in text_list:
            if element in '([{':
                Stack(help_list).push(element)
            elif element in ')]}':
                if element == ')':
                    anti_el = '('
                elif element == ']':
                    anti_el = '['
                elif element == '}':
                    anti_el = '{'
                if (element == ')' and help_list.count(anti_el) > 0) or (element == ']' and anti_el in help_list)\
                        or (element == '}' and help_list.count(anti_el) > 0):
                    Stack(text_list_copy).remove(element)
                    Stack(text_list_copy).remove(anti_el)
                    help_list.remove(anti_el)
                else:
                    return "Несбалансированно"
        if Stack(text_list_copy).isEmpty() == True:
            return 'Сбалансированно'
    else:
        return "Несбалансированно"

def check_balance_2(text):
    ''' Функция также решает задачу на проверку сбалансированности скобок, но без использования функций класса Stack:
    size, push, remove. Но работает по другой логике.
    '''
    if len(list(text)) % 2 == 0 and text[0] in '([{' and text[-1] in '}])':
        if text.count('(') == text.count(')') and text.count('[') == text.count(']') and text.count('{') == text.count('}'):
            haf = len(text) // 2
            if (text[:haf].count('(') >= text[:haf].count(')')) and (text[haf:].count(')') >= text[haf:].count('(')):
                if (text[:haf].count('[') >= text[:haf].count(']')) and (text[haf:].count(']') >= text[haf:].count('[')):
                    if (text[:haf].count('{') >= text[:haf].count('}')) and (
                            text[haf:].count('}') >= text[haf:].count('{')):
                        return 'Сбалансированно'
                    else:
                        return "Несбалансированно"
                else:
                    return "Несбалансированно"
            else:
                return "Несбалансированно"
        else:
            return "Несбалансированно"
    else:
        return "Несбалансированно"


if __name__ == "__main__":

    str_1 = '(((([{}]))))'
    stack_user = Stack(stack_list=list(str_1))
    str_2 = '[([])((([[[]]])))]{()}'
    str_3 = '{{[()]}}'
    str_4 = '}{}'
    str_5 = '{{[(])]}}'
    str_6 = '[[{())}]'

    print('Проверка работы функции с использованием класса Stack:')
    print(str_1, check_balance(str_1))
    print(str_2, check_balance(str_2))
    print(str_3, check_balance(str_3))
    print(str_4, check_balance(str_4))
    print(str_5, check_balance(str_5))
    print(str_6, check_balance(str_6))
    print()
    print('Проверка работы функции без использования класса Stack:')
    print(str_1, check_balance_2(str_1))
    print(str_2, check_balance_2(str_2))
    print(str_3, check_balance_2(str_3))
    print(str_4, check_balance_2(str_4))
    print(str_5, check_balance_2(str_5))
    print(str_6, check_balance_2(str_6))