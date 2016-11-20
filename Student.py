class Student(object):
	def __init__(self,stud_descr, subject_count):
		self.stud_descr = stud_descr.split(' ')
		self.name = self.stud_descr[0]
		self.surname = self.stud_descr[1]
		self.subject_count = subject_count

	def get_name(self):
		return self.name

	def get_surname(self):
		return self.surname
