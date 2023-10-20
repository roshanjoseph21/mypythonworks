f1=open("C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\fileoepration\\allstudents.txt")
f2=open("C:\\Users\\My\\OneDrive\\Desktop\\my_pythonworks\\fileoepration\\failed.txt")

all_students={line.rstrip("\n") for line in f1}
failed_students={line.rstrip("\n") for line in f2}

passed_student= all_students.difference(failed_students)
print(passed_student)