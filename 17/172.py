#cd D:python/python/17
#172.py
#3.	Напишите в классе Student метод-инвариант класса.

class Rocket:

	def __init__(self, fuil):
		self.fuil = fuil

	def print(self):
		print ("Топливо: ")
		return (str(self.fuil + " л"))

	def chek(self):
		statik = True
		if self.fuil == str(self.fuil):
			statik = True
		else:
			statik = False

		print(statik)

b = input("Fuil: ")

roket = Rocket(b)

roket.chek()