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


class Subject(object):
	def __init__(self,sub_name):
		self.sub_name = sub_name

	def get_sub_name(self):
		return self.sub_name


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
