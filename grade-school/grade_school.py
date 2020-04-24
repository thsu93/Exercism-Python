class School:
    students = {}
    
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, grade):
        self.students[name] = grade

    def roster(self):
        templist = sorted(self.students.items(), key = lambda kv:(kv[1],kv[0]))
        return ([i[0] for i in templist])

    def grade(self, grade_number):
        templist = sorted(self.students.items(), key = lambda kv:(kv[1],kv[0]))
        return ([i[0] for i in templist if i[1] == grade_number])
