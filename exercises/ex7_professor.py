from ex7_person import Person

class Professor(Person):

    def __init__(self, first_name, last_name, age, subjects=[]):
        super().__init__(first_name, last_name, age)
        self.subjects = subjects
    
    def list_subjects(self):
        for subject in self.subjects:
            print(f" - {subject}")
    
    def add_subject(self, subject):
        self.subjects.append(subject)
    
    def remove_subject(self, subject):
        self.subjects.remove(subject)
