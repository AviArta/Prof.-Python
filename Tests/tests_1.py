import unittest
from mock import patch
from parameterized import parameterized
from Tests.HW_Tests_code import define_name_upg, define_dir_upg, add_doc_upg, delete_doc_upg, change_dir_upg, add_dir_upg,\
    define_name


class TestFunction(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('setUp ==>')

    # def tearDown(self) -> None:
    #     print('tearDown ==>')

# тест функции, которая принимает номер документа и выводит имя человека, которому он принадлежит
    @parameterized.expand(
        [
            ("2207 876234", "Документ на имя: Василий Гупкин."),
            ("11-2", "Документ на имя: Геннадий Покемонов."),
            ("10006", "Документ на имя: Аристарх Павлов."),
            ("000100", "Документа номер 000100 нет.")
        ]
    )
    def test_define_name_upg(self, number_doc, result):
        function_result = define_name_upg(number_doc)
        self.assertEqual(function_result, result)


# тест функции, которая принимает номер документа и выводит номер полки, на которой он находится
    @parameterized.expand(
        [
            ("2207 876234", "Документ на 3 полке."),
            ("11-2", "Документ на 1 полке."),
            ("10006", "Документ на 2 полке."),
            ("000100", "Документа номер 000100 нет.")
        ]
    )
    def test_define_dir_upg(self, number_doc, result):
        function_result = define_dir_upg(number_doc)
        self.assertEqual(function_result, result)

# тест функции, которая принимает инф. по новому документу и добавляет новый документ на полку:
    @parameterized.expand(
        [
            ("pasport ", "1400 111000", "Маринина Марина", "1", "Документ (pasport  1400 111000 на имя Маринина Марина) добавлен в базу и расположен на полке 1."),
            ("pasport ", "1400 111000", "Маринина Марина", "6", "Такой полки нет.")
        ]
    )
    def test_add_doc_upg(self, type_add, number_add, name_add, dir_add, result):
        function_result = add_doc_upg(type_add, number_add, name_add, dir_add)
        self.assertEqual(function_result, result)

# тест функции, которая принимает номер документа и удаляет его из каталога и из перечня полок.
    @parameterized.expand(
        [
            ("2207 876234", "Документ номер 2207 876234 удалён."),
            ("000100", "Документа номер 000100 нет.")
        ]
    )
    def test_delete_doc_upg(self, number_doc, result):
        function_result = delete_doc_upg(number_doc)
        self.assertEqual(function_result, result)

# тест функции, которая принимает номер документа и целевую полку и перемещает его с текущей полки на целевую:
    @parameterized.expand(
        [
            ("2207 876234", "3", "Документ номер 2207 876234 перемещён на полку 3."),
            ("2207 876234", "4", "Полки номер 4 нет."),
            ("0012200", "2", "Документа номер 0012200 нет.")
        ]
    )
    def test_change_dir_upg(self, number_doc, new_dir, result):
        function_result = change_dir_upg(number_doc, new_dir)
        self.assertEqual(function_result, result)

# тест функции, которая принимает номер новой полки и добавляет ее в перечень:
    @parameterized.expand(
        [
            ("10", "Полка номер 10 добавлена."),
            ("3", "Полка номер 3 уже существует.")
        ]
    )
    def test_add_dir_upg(self, new_dir, result):
        function_result = add_dir_upg(new_dir)
        self.assertEqual(function_result, result)