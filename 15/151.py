#cd D:python/python/15
#151.py
#Напишите простой контейнерный класс для небольшой фирмы, 
#в которой работает администратор, служащий и рабочий – 
#производные объекты от общего базового класса. 

class Person:

	def set(self, name, surname, proffesion):

		self._protected_member = name
		self._protected_member = surname
		self._protected_member = proffesion


	def __init__(self, name, surname, proffesion, ):

		self.name = name
		self.surname = surname
		self.proffesion = proffesion

	def choice(self):

		Conteiner = []

		if (self.proffesion == 1):

			x = input("Количество клментов: ")
			clients = x
			Conteiner.append(self.name)
			Conteiner.append(self.surname)
			Conteiner.append(clients)
			print(Conteiner)

		elif(self.proffesion == 2):

			x = input("Количество рабочих дней: ")
			workday = x
			Conteiner.append(self.name)
			Conteiner.append(self.surname)
			Conteiner.append(workday)
			print(Conteiner)


		elif(self.proffesion == 3):

			x = input("Зарплата: ")
			salary = x
			Conteiner.append(self.name)
			Conteiner.append(self.surname)
			Conteiner.append(salary)
			print(Conteiner)





a, b = input("Имя, Фамилия: ").split()
c = int(input("Професия: 1 - Администратор, 2 - Рабочий, 3 - Служащий: "))
Pr1 = Person(a, b, c)
Pr1.choice()