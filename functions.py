students = []


def print_student():
    for student in students:
        print("No: {0} - Name: {1}"
              .format(student.get("name", "Not Found Student Name"),
                      student.get("student_id", "Not Found Student No")
                      ))


def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


print("Adding students...")
add_student("Mark", 12)
print("Mark added.")
add_student("Josef", 32)
print("Josef added.")
print("Added all students...")
print("Students:")
print_student()
print("Total student count: {0}".format(len(students)))
