import json
from datetime import datetime

def dec_logger(max_size):

    def dec_logger_(old_function):
        LOG_dict = {}

        def new_function(*args, **kwargs):
            time_start_func = str(datetime.now())
            result = old_function(*args, **kwargs)

            if len(LOG_dict) > max_size:
                LOG_dict.pop(list(LOG_dict)[0])
                print('Превышен max размер словаря, поэтому далён начальный элемент и добавлен текущий.')

            LOG_dict[time_start_func] = f"функция {old_function.__name__} вызвана с аргументами {args}, результат = {result}."

            with open('res_decor.json', 'w', encoding='utf-8') as file:  # , encoding='utf-8'
                file.write(json.dumps(LOG_dict, ensure_ascii=False, indent=4))
                print('Запись в файл прошла успешно.')

            return result
        return new_function
    return dec_logger_


@dec_logger(2)
def summator_int(*args):
    print(f"Выполняется функция summator_int с аргументами {args}.")
    return f"Результат функции = {sum(args)}."


if __name__ == '__main__':
    print(summator_int(1, 10, 100))
    print()
    print(summator_int(2, 20, 200))
    print()
    print(summator_int(3, 30, 300))
    print()
    print(summator_int(4, 40, 400))

