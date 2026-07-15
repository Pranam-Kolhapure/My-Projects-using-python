class Student:

	#These are class variables
	class_year = 2025
	num_students = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Student.num_students +=1

stud1 = Student("Jaime", 35)
stud2 = Student("Robb",19)
stud3 = Student("Stannis",27)
stud4 = Student("Eddard",41)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(stud1.name)
print(stud2.name)
print(stud3.name)
print(stud4.name)

