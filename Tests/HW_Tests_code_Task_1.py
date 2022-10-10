documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "7914 112214", "name": "Вастльева Катерина"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '7914 112214'],
    '3': []
}


# спросит номер документа и выведет имя человека, которому он принадлежит:
def define_name():
    number_doc = input('Введите номер документа: ')
    for document in documents:
        if number_doc == document['number']:
            return f"Документ на имя: {document['name']}."
    return f"Документа номер {number_doc} нет."
# print(define_name())

# версия функции для теста без инпута:
def define_name_upg(number_doc):
    for document in documents:
        if number_doc == document['number']:
            return f"Документ на имя: {document['name']}."
    return f"Документа номер {number_doc} нет."


# спросит номер документа и выведет номер полки, на которой он находится:
def define_dir():
    number_doc = input('Введите номер документа: ')
    for document in documents:
        if number_doc == document['number']:
            for dir, doc in directories.items():
                if number_doc in doc:
                    # print(directories)
                    return f"Документ на {dir} полке."
    return f"Документа номер {number_doc} нет."
# print(define_dir())


# версия функции для теста:
def define_dir_upg(number_doc):
    for document in documents:
        if number_doc == document['number']:
            for dir, doc in directories.items():
                if number_doc in doc:
                    return f"Документ на {dir} полке."
    return f"Документа номер {number_doc} нет."


# выведет список всех документов в формате passport "2207 876234" "Василий Гупкин":
def define_all():
    # doc_all = []
    for document in documents:
        print(f"""{document["type"]} '{document['number']}' '{document['name']}'""")
# define_all()


# добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_doc():
    type_add = input('Введите тип документа: ')
    number_add = input('Введите номер документа: ')
    name_add = input('Введите имя и фамилию держателя документа: ')
    dir_add = input('Введите номер полки для хранения документа: ')
    for dir in directories.keys():
        if dir_add == dir:
            newdoc_dict = {}
            newdoc_dict['type'] = type_add
            newdoc_dict['number'] = number_add
            newdoc_dict['name'] = name_add
            documents.append(newdoc_dict)
            directories[dir_add] += number_add.split()
            # print(documents, directories)
            return f"Документ ({type_add} {number_add} на имя {name_add}) добавлен в базу и расположен на полке {dir_add}."
    return f"Такой полки нет."
# print(add_doc())


# вариант функции для тестирования:
def add_doc_upg(type_add, number_add, name_add, dir_add):
    for dir in directories.keys():
        if dir_add == dir:
            newdoc_dict = {}
            newdoc_dict['type'] = type_add
            newdoc_dict['number'] = number_add
            newdoc_dict['name'] = name_add
            documents.append(newdoc_dict)
            directories[dir_add] += number_add.split()
            # print(documents, directories)
            return f"Документ ({type_add} {number_add} на имя {name_add}) добавлен в базу и расположен на полке {dir_add}."
        else:
            return f"Такой полки нет."
print(add_doc_upg("pasport ", "1400 111000", "Маринина Марина", "1"))


# спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
def delete_doc():
    number_doc = input('Введите номер документа: ')
    for document in documents:
        if number_doc == document['number']:
            for dir, doc in directories.items():
                if number_doc in doc:
                    documents.remove(document)
                    doc.remove(number_doc)
                    # print(documents, directories)
                    return f"Документ номер {number_doc} удалён."
        else:
            return f"Документа номер {number_doc} нет."
# print(delete_doc())
# print(documents)

# вариант функции для тестирования:
def delete_doc_upg(number_doc):
    for document in documents:
        if number_doc == document['number']:
            # for dir, doc in directories.items():
            #     if number_doc in doc:
                documents.remove(document)
                # doc.remove(number_doc)
                return f"Документ номер {number_doc} удалён."
        else:
            return f"Документа номер {number_doc} нет."
# print(delete_doc_upg("7914 112214"))

# спросит номер документа и целевую полку и переместит его с текущей полки на целевую:
def change_dir():
    number_doc = input('Введите номер документа: ')
    for document in documents:
        if number_doc == document['number']:
            new_dir = input('Введите номер полки, на которую переместить документ: ')
            for dir, doc in directories.items():
                if new_dir not in directories.keys():
                    return f"Полки номер {new_dir} нет."
                elif number_doc in doc:
                    doc.remove(number_doc)
                    directories[new_dir].append(number_doc)
            print(directories)
            return f"Документ номер {number_doc} перемещён на полку {new_dir}."
    return f"Документа номер {number_doc} нет."
# print(change_dir())


# вариант функции для тестирования:
def change_dir_upg(number_doc, new_dir):
    for document in documents:
        if number_doc == document['number']:
            for dir, doc in directories.items():
                if new_dir not in directories.keys():
                    return f"Полки номер {new_dir} нет."
                elif number_doc in doc:
                    doc.remove(number_doc)
                    directories[new_dir].append(number_doc)
                    return f"Документ номер {number_doc} перемещён на полку {new_dir}."
        else:
            return f"Документа номер {number_doc} нет."


# спросит номер новой полки и добавит ее в перечень:
def add_dir():
    new_dir = input('Введите номер новой полки: ')
    if new_dir not in directories.keys():
        directories[new_dir] = []
        # print(directories)
        return f"Полка номер {new_dir} добавлена."
    return f"Полка номер {new_dir} уже существует."
# print(add_dir())


# вариант функции для тестирования:
def add_dir_upg(new_dir):
    if new_dir not in directories.keys():
        directories[new_dir] = []
        return f"Полка номер {new_dir} добавлена."
    else:
        return f"Полка номер {new_dir} уже существует."


# итоговая функция
def collect_commands():
    help_prog = """HELP:
  'p' - узнать имя человека по номеру документа.
  's' - узнать номер полки по номеру документа.
  'l' - список всех документов.
  'a' - добавить новый документ на нужную полку.
  'd' - удаление документа.
  'm' - переместить документ.
  'as' - добавить новую полку.
  'q' - выход.
  """
    print(help_prog)
    while True:
        command = input("Введите команду: ")
        command_dict = {'p': define_name, 's': define_dir, 'l': define_all, 'a': add_doc, 'd': delete_doc,
                        'm': change_dir, 'as': add_dir}
        if command in command_dict.keys():
            value = command_dict[command]
            print(value())
            continue
        elif command == 'q':
            print('Выход из программы.')
            break
        else:
            print('Такой команды нет. Попробуйте ещё раз.')
            continue


# if __name__ == '__main__':
#     collect_commands()