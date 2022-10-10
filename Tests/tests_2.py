import pytest
from .HW_tests_code_Task_2 import YaUploader, YA_TOKEN

# Тест на создание папки.
fixture_create_new_folder = [
    ("/HW_Tests_folder", 409),
    ("/HW_Tests", 201)
]


@pytest.mark.parametrize('dir_ya, right_result', fixture_create_new_folder)
def test_create_new_folder(dir_ya, right_result):
    instanse = YaUploader(ya_token=YA_TOKEN)
    function_result = instanse.create_new_folder(dir_ya)
    assert function_result == right_result


# Тест на наличие папки в списке папок Я.Диска.
fixture_check_folder_in_folders_list = [
    ("HW_Tests_folder", 409),
    ("HW_", 201)
]


@pytest.mark.parametrize('dir_ya, right_result', fixture_check_folder_in_folders_list)
def test_check_folder_in_folders_list(dir_ya, right_result):
    instanse = YaUploader(ya_token=YA_TOKEN)
    function_result = instanse.create_new_folder(dir_ya)
    assert function_result == right_result


# Тест на даление папки в списке папок Я.Диска.
fixture_delete_folder = [
    ("HW_Tests", 204),
    ("HW_", 204)
]


@pytest.mark.parametrize('dir_ya, right_result', fixture_delete_folder)
def test_delete_folder(dir_ya, right_result):
    instanse = YaUploader(ya_token=YA_TOKEN)
    function_result = instanse.delete_folder(dir_ya)
    assert function_result == right_result

