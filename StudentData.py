class StudentData(object):
	def __init__(self, grades, attendances):
		self.grades = grades
		self.attendances = attendances
		self.total_avg = sum(sum(i)/8 for i in zip(*self.grades))/6

	def get_grades(self):
		return self.grades

	def get_grade(self,index):
		return self.grades[index]

	def get_attendances(self):
		return self.attendances

	def get_attendance(self, index):
		return self.attendances[index]

	def get_subject_average(self):
		return sum(self.grades)/len(self.grades)

	def get_total_avg(self):
		return self.total_avg
