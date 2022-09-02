import re
import csv
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
def file_reader():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    result_list = contacts_list.copy()
    return result_list

# TODO 1: выполните пункты 1-3 ДЗ

# ДЗ 1: поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
def corr_name():
  result_name_list = file_reader()
  for el in result_name_list:
      if el[0].count(' ') == 1:
        h_list = el[0].split()
        el[0], el[1] = h_list[0], h_list[1]
      elif el[0].count(' ') == 2:
        h_list = el[0].split()
        el[0], el[1], el[2] = h_list[0], h_list[1], h_list[2]
      elif el[1].count(' ') == 1:
        h_list = el[1].split()
        el[1], el[2] = h_list[0], h_list[1]
  return result_name_list

# ДЗ 2: привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
def corr_phone_number():
    pattern = r"(\+7|8)\s*\(?(\d{3})\)? ?-?(\d{3})-?(\d{2})-?(\d{2}) ?\(?(доб.)?\s*((\d+))?\)?"
    sub1 = r"+7(\2)\3-\4-\5"
    sub2 = r"+7(\2)\3-\4-\5 доб.\8"
    result_phone_list = corr_name()
    for el in result_phone_list:
        for phone in el:
            if re.findall(pattern, phone):
                if 'доб.' in phone:
                    corr_number = re.sub(pattern, sub2, phone)
                    ind = el.index(phone)
                    el[ind] = corr_number
                else:
                    corr_number = re.sub(pattern, sub1, phone)
                    ind = el.index(phone)
                    el[ind] = corr_number
    return result_phone_list

# ДЗ 3: объединить все дублирующиеся записи о человеке в одну.
def join_duplicate_name():
  result_list = corr_phone_number()
  result_no_dubl_list = []
  help_name_list = []
  for el in result_list:
      if [el[0], el[1]] not in help_name_list:
          help_name_list.append([el[0], el[1]])
          result_no_dubl_list.append(el)
      else:
          ind = help_name_list.index([el[0], el[1]])
          result_no_dubl_list[ind].extend(el)
          help_list = []
          for element in result_no_dubl_list[ind]:
              if element not in help_list:
                help_list.append(element)
          result_no_dubl_list[ind] = help_list
  return result_no_dubl_list


# TODO 2: сохраните получившиеся данные в другой файл

# код для записи файла в формате CSV
def result_file_writer():
    with open("phonebook_result.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(join_duplicate_name())
    print('Запись корректной телефонной книги в результирующий файл завершена.')