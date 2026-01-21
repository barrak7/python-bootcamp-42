from new_student import Student

student = Student(name="Edward", surname="agle")

print(student)

# should throw a TypeError
student = Student(name="Edward", surname="agle", id="toto")

print(student)
