#cd D:python/python/22
#221.py
#Используя ранее разработанные иерархии классов (Animal, 
#Transport, Worker, Student…), создайте в программе общий 
#контейнер (массив, вектор, список…) объектов различных типов.

class Transport:

	def set(self, number, date, mark):
		self._protected_member = number
		self._protected_member = date
		self._protected_member = mark


	def __init__(self, number, date, mark):
		self.number = number
		self.date = date
		self.mark = mark

	def print(self):
		return ("Номер:", self.number,"Год выпуска: ", self.date, "Марка: ", self.mark)


class Car(Transport):

	def set(self, speed):
		self._protected_member = speed

	def __init__(self, sp):
		self.speed = sp

	def print(self):
		return ("Максимальная скорость: ", str(self.speed) +  " км/час")


class Bus(Transport):

	def set(self, seats):
		self._protected_member = seats

	def __init__(self, st):
		self.seats = st

	def print(self):
		return ("Число посадочных мест: ", self.seats)




class Person:

	def set(self, name, surname, proffesion):

		self._protected_member = name
		self._protected_member = surname
		self._protected_member = proffesion


	def __init__(self, name, surname, proffesion, ):

		self.name = name
		self.surname = surname
		self.proffesion = proffesion
		self.clients = 0
		self.workday = 0
		self.salary = 0

	def choice(self):
		if (int(self.proffesion) == 1):
			x = input("Количество клментов: ")
			self.clients = x

		elif(int(self.proffesion) == 2):
			x = input("Количество рабочих дней: ")
			self.workday = x


		elif(int(self.proffesion) == 3):
			x = input("Зарплата: ")
			self.salary
			

	def print(self):
		if(int(self.proffesion) == 1):
			return("Имя:", self.name, "Фамилия:", self.surname, "К-ство клиентов:", self.clients)

		elif(int(self.proffesion) == 2):
			return ("Имя:", self.name, "Фамилия:", self.surname, "К-ство рабочих дней:", self.workday)

		elif(int(self.proffesion) == 3):	
			return ("Имя:", self.name, "Фамилия:", self.surname, "Зарплата:", self.salary)
		else:
			return ("Имя:", self.name, "Фамилия:", self.surname)


Conteiner = []

h = int(input("0 - трaнспорт, 1 - сотрудник:  "))

if h == 0:
	a = int(input ("Номер: "))
	b = int(input ("Год выпуска: "))
	c = str(input ("Марка: "))
	d = int(input("1 = машына, 0 = автобус: "))

	Tr = Transport(a, b, c)
	

	if d == 1:

		x = int(input ("Максимальная скорость: "))
		Cr = Car(x)
		Conteiner.append(Cr.print())
		Conteiner.append(Tr.print())

	elif d == 0:
		y = int(input ("Число посадочных мест: "))
		Bs = Bus(y)
		Conteiner.append(Bs.print())
		Conteiner.append(Tr.print())

elif h == 1:
	name = input("Имя: ")
	surname = input("Фамилия: ")
	proffesion = input("Професия: 1 - Администратор, 2 - Рабочий, 3 - Служащий: ")

	Pr1 = Person(name, surname, proffesion)
	Pr1.choice()
	Conteiner.append(Pr1.print())
	print()

else:
		print("error")


print(Conteiner)