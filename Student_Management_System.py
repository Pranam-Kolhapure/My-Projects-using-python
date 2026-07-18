import json
import os


class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }


class StudentManager:
    def __init__(self):
        self.filename = "students.json"
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.students = json.load(file)

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["student_id"] == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(student_id, name, age, course)
        self.students.append(student.to_dict())
        self.save_data()

        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n------ Student List ------")
        for student in self.students:
            print(f"ID     : {student['student_id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print("-" * 30)

    def search_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["student_id"] == student_id:
                print("\nStudent Found")
                print(student)
                return

        print("Student not found.")

    def update_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["student_id"] == student_id:
                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["course"] = input("Enter New Course: ")

                self.save_data()
                print("Student updated successfully!")
                return

        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["student_id"] == student_id:
                self.students.remove(student)
                self.save_data()
                print("Student deleted successfully!")
                return

        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
