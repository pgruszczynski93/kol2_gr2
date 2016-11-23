from Student import *
import random

total_avgs = []

def generate_grades_attendances(students, subject_count, stud_data_list):
	for stud in students:
		grades = [[random.randint(2,5) for x in range(8)] for i in range(subject_count)]
		attendances = [[random.randint(0,1) for x in range(8)] for i in range(subject_count)] 
		stud_data_list.append(StudentData(grades,attendances))
		grades = []
		attendances = []
			
def fill_diary(diary, students, subjects, stud_data_list):
	sub_grades = []
	sub_attendances = []
	sub_stud_list = []
	sub_key = ""
	stud_key = ""

	sub_grades = [[stud_data_list[j].get_grades()[i] for i in range(len(subjects))] for j in range(len(students))]
	sub_attendances = [[stud_data_list[j].get_attendances()[i] for i in range(len(subjects))] for j in range(len(students))]

	for i in range(len(subjects)):
		sub_key = subjects[i].get_sub_name()
		for j in range(len(students)):
			stud_key = students[j].get_name()+" "+students[j].get_surname()
			sub_stud_list.append({stud_key:[sub_grades[j][i],sub_attendances[j][i]]})
		diary[sub_key] = sub_stud_list
		sub_stud_list = []


def count_avg(grades):
	return sum(grades)/len(grades)

def final_grade(avg):
	return round(avg)

def count_presence(presence):
	return presence.count(1)

def total_presence(presence):
	return len(presence)

def sub_diary(stud_data):
	for stud in stud_data:
   		print("Imie i nazwisko: ",stud)
   		print("Oceny: ",stud_data[stud][0])
   		print("Srednia ocena z przedmiotu: "+str(count_avg(stud_data[stud][0])))
   		print("Ocena koncowa: "+str(final_grade(count_avg(stud_data[stud][0]))))
   		print("Obecnosci: ",stud_data[stud][1])
   		print("Ilosc obecnosci: "+str(count_presence(stud_data[stud][1]))+"/"+str(total_presence(stud_data[stud][1])))
   		print()


def print_diary(diary,students):
	print("============================================================================")
	print("============================= Dziennik lekcyjny ============================")
	print("============================================================================")
	for subject in diary:
   		print ("\n********** Przedmiot: "+subject+" **********\n")
   		i = 0
   		for stud_data in diary[subject]:
   			sub_diary(stud_data)
	   		i+=1

def all_stats(stud_data_list):
	print("============================================================================")
	print("============================= Podsumowanie =================================")
	print("============================================================================")
	print("Srednie koncowe")
	i = 1
	for sdl in stud_data_list:
		print("%d %f"%(i,sdl.get_total_avg()))
		i+=1
