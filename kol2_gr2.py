#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

from Student import *
from Subject import *
from StudentData import *
from TestLibrary import *

def main():	
	diary = {}
	stud_data_list = []

	subject_names = ["C++","Grafika 3D","Matematyka","Fizyka","Inzynieria Oprogramowania","Wizualizacja i Grafika Komputerowa"]
	stud_list = ["Ala Makota","Ola Maale","Michal Sek", "Olaf Kes","Milosz Mily","Aleksander Dziewonski","Martyna Potyka","Przemyslaw Gruszczynski"]
	
	subject_count = len(subject_names)
	subjects = [Subject(name) for name in subject_names]
	students = [Student(description,subject_count) for description in stud_list]

	generate_grades_attendances(students, subject_count, stud_data_list)
	fill_diary(diary, students, subjects, stud_data_list)
	print_diary(diary,students)
	all_stats(stud_data_list)
	
if __name__ == "__main__":
	main()
