from ex7_student import Student
from ex7_professor import Professor
from ex7_lecture import Lecture

# Professor
professor = Professor("Linda", "Gray", 42, ['Linux', 'Databases'])
professor.print_name()
professor.add_subject('Programming')
professor.remove_subject('Linux')
professor.list_subjects()

# Lecture
linux_lecture = Lecture("Basic Linux Commands", 25, 45)
linux_lecture.print_info()

python_lecture = Lecture("Programming with Python", 12, 60)
python_lecture.add_professor(professor)

database_lecture = Lecture("MySQL Database Administration", 15, 90)
database_lecture.add_professor(professor)

kubernetes_lecture = Lecture("Kubernetes for Beginners", 10, 60)

# Student
student = Student("Peter", "Smith", 24, [linux_lecture, python_lecture, database_lecture])
student.print_name()
student.add_lecture(kubernetes_lecture)
student.remove_lecture("MySQL Database Administration")
student.list_lectures()
