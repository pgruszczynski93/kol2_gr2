class Student(object):
	def __init__(self,name,surname,scores,attendances):
		self.name = name
		self.surname = surname
		self.scores = scores
		self.attendances = attendances
		

	def get_name(self):
		return self.name

	def get_surname(self):
		return self.surname

	def show_student(self):
		print("Imie %s, Nazwisko %s"%(self.get_name(), self.get_name()))

	def get_scores(self):
		print("Oceny studenta z przedmiotow %s %s"%(self.get_name(),self.get_surname()))
		for score in self.scores:
			print (score),

	def get_attendances(self):
		print("Obecnosc studenta %s %s"%(self.get_name(),self.get_surname()))
		for attendance in self.attendances:
			print (attendance),
	
	def avg_total(self):
		print sum(self.scores)/len(self.scores)

	
	def avg_subject(self):
		pass
