class Lecture:

    def __init__(self, name, max_students, duration, professors=[]):
        self.name = name
        self.max_students = max_students
        self.duration = duration
        self.professors = professors
    
    def print_info(self):
        print(f"{self.name} ({self.duration} minutes)")
    
    def add_professor(self, professor):
        self.professors.append(professor)
