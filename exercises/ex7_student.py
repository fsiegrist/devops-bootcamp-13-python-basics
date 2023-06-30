from ex7_person import Person

class Student(Person):

    def __init__(self, first_name, last_name, age, lectures=[]):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures
    
    def list_lectures(self):
        for lecture in self.lectures:
            print(f" - {lecture.name}")
    
    def add_lecture(self, lecture):
        self.lectures.append(lecture)
    
    def remove_lecture(self, name_of_lecture_to_remove):
        lecture_to_be_removed = None
        for lecture in self.lectures:
            if lecture.name == name_of_lecture_to_remove:
                lecture_to_be_removed = lecture
                break
        if lecture_to_be_removed != None:
            self.lectures.remove(lecture_to_be_removed)
