#cd D:python/python/17
#171.py
#Напишите операторы защиты от дублирования для заголовочного файла Student.h.

from collections import OrderedDict

file = open("file.txt", "w")

name = ["vlad", "maks", "igor"]

nameCopy = ["vlad", "maks", "igor"]

newName  = ["Anya", "Egor", "Danil"]

def check(a=[], b=[]):
	for i in name:
		file.write(i)

	private = 0
	if a == b:
		private = 1

	else:
		private = 0

	if private == 1:
		print("Повтор")

	else:
		print("Нет повтора")
		for i in b:
			file.write(i)
		private = 0

check(name, nameCopy)
check(name, newName)