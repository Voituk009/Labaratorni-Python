#cd D:python/python/15
#155.py
#Напишите главную программу, 
#выполняющую создание и обработку объекта типа фирма.


class Person:

	global Conteiner 
	Conteiner = []

	
	def set(self, name, surname, proffesion):

		self._protected_member = name
		self._protected_member = surname
		self._protected_member = proffesion


	def __init__(self, name, surname, proffesion):

		self.name = name
		self.surname = surname
		self.proffesion = proffesion

	def choice(self):


		if (self.proffesion == 1):

			x = input("Количество клментов: ")
			clients = x
			Conteiner.append(self.name)
			Conteiner.append(self.surname)
			Conteiner.append(clients)


		elif(self.proffesion == 2):

			x = input("Количество рабочих дней: ")
			workday = x
			Conteiner.append(self.name)
			Conteiner.append(self.surname)
			Conteiner.append(workday)



		elif(self.proffesion == 3):

			x = input("Зарплата: ")
			salary = x
			Conteiner.append(self.name)
			Conteiner.append(self.surname)
			Conteiner.append(salary)


	def vacation(self):

		y = int(input("Работник в отпуске?: 1 - да, 0 - нет: "))

		v = "В отпуске"

		if (y == 1):
			Conteiner.append(v)
			print(Conteiner)

		elif (y == 0):
			print(Conteiner)



a, b = input("Имя, Фамилия: ").split()
c = int(input("Професия: 1 - Администратор, 2 - Рабочий, 3 - Служащий: "))
Pr1 = Person(a, b, c)
Pr1.choice()
Pr1.vacation()