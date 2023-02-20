class Program:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.students = {}

    def enroll(self, student):
        self.students[student.name] = student
        
    def __repr__(self):
        description="""
        name = {}
        code = {}
        """.format(self.name,self.code)
        return description

class Student:
    def __init__(self, name):
        self.name = name
        self.programs = {}

    def enroll(self, program):
        self.programs[program.code] = program
        program.enroll(self)

programs = {}
# create some Program objects
cs_program = Program("Computer Science", "CS101")
math_program = Program("Mathematics", "MATH101")

programs[cs_program.code] = cs_program
programs[math_program.code] = math_program
#print(list(programs))
for program in programs.values():
    print(program.code)


# create some Student objects and enroll them in some programs
student1 = Student("John Doe")
student1.enroll(cs_program)
student1.enroll(math_program)

student2 = Student("Jane Doe")
student2.enroll(cs_program)

student3 = Student("Bob Smith")
student3.enroll(math_program)

# get a list of students enrolled in the Computer Science program
cs_students = list(cs_program.students.keys())

print("Students enrolled in Computer Science:", cs_students)
