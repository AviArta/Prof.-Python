nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None]]

# решение без рекурсии:
def Flat_Generator(list_):
	index_el = 0
	index_el2 = -1
	while index_el2 <= len(list_[index_el]) - 1:
		if index_el2 < len(list_[index_el]) - 1:
			index_el = index_el
			index_el2 += 1
			yield list_[index_el][index_el2]
		elif index_el2 == len(list_[index_el]) - 1:
			index_el += 1
			index_el2 = 0
			if index_el <= len(list_) - 1:
				yield list_[index_el][index_el2]
			else:
				break
	else:
		if index_el > len(list_) - 1 or index_el2 > len(list_[index_el]) - 1:
			raise StopIteration

# решение с рекурсией:
def Flat_Generator_1(list_, depth=0):
	for element in list_:
		if type(element) == list:
			Flat_Generator_1(element, depth+1)
		else:
			print (element)

# решение с любым уровнем вложенности:
def Flat_Generator_2(list_):
	for element in list_:
		if type(element) != list:
			yield element
		else:
			for i in Flat_Generator_2(element):
				yield i


if __name__ == '__main__':

	print("Без рекурсии: ")
	for item in Flat_Generator(nested_list):
		print(item)

	print()
	print("Через рекурсию: ")
	Flat_Generator_1(nested_list)

	print()
	print("Эадача с *: ")

	for item in Flat_Generator(nested_list):
		print(item)
