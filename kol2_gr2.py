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

def main():
	stud = Student("Ala","Makota",[2,3,4,5],[1,1,0])
	stud.get_scores()
	print("\nSrednia: ")
	stud.avg_total()
	stud.get_attendances()

	stud = Student("KAla","VaMakota",[2,3,4,5,4,5,4,2],[1,1,0,1,1])
	stud.get_scores()
	print("\nSrednia: ")
	stud.avg_total()
	stud.get_attendances()

	
	stud = Student("AsAla","Sama",[2,3,4,5,2,3,4,5,4,2,2,1,1,4],[1,1,0])
	stud.get_scores()
	print("\nSrednia: ")
	stud.avg_total()
	stud.get_attendances()

	
if __name__ == "__main__":
	main()
