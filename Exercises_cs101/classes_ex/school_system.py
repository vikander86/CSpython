#Creating a school system, with students,programs and teachers
#We need 3classes - student,program,teacher

#we need info about the students, name etc, and what programs they are enrolled in.
#we need info about the programs, who's enrolled and who the teacher is
#we need info about the teacher, name etc and what programs they are teaching.


class Student:
    def __init__(self,name,age,email,pers_num):
        self.name = name
        self.age = age
        self.email = email
        self.personalnumber = str(pers_num)
        self.programs = {}
    
    def __repr__(self):
        program_names = [program.name for program in self.programs.values()]
        program_list = ", ".join(program_names)
        
        description = """
        Student name: {name}
        Student age: {age}
        Student email: {email}
        Student personalnumber: {pers_num}
        Student program(s): {programs}
            """.format(name=self.name,age=self.age,email=self.email,pers_num= "*****"+self.personalnumber[-4:],programs= program_list)
        return description
    
    def enroll_student(self,program):
        self.programs[program.code] = program
        program.enroll(self)
            
        

class Teacher:
    def __init__(self,name,contact_info):
        self.name = name
        self.contact_info = contact_info
        self.programs = []
    
    def __repr__(self):
        pass
    
    def course(self,program):
        self.programs.append(program)

class Program:
    def __init__(self,name,code,teacher):
        self.name = name
        self.code = code
        self.teacher = teacher
        self.students = {}
        
    def __repr__(self):
        description = """
        Program name: {}
        Program code: {}
        Program teacher: {}
        """.format(self.name,self.code,self.teacher)
        return description
    
    def enroll(self, student):
        self.students[student.name] = student
           

programs = {}
students = []
teachers = []
#initializing a programs list
program_list = [
    Program("Computer Science", "CS101", "John Kusack"),
    Program("Mathematics", "MATH101", "Billy Bob"),
    Program("Physics", "PHYS101", "Jane Smith"),
    Program("Chemistry", "CHEM101", "Bob Johnson"),
    Program("English", "ENG101", "Sarah Lee"),
    Program("History", "HIST101", "Tom Brown")
]
#add programs to the programs dict, assigning the program.code to the key
for program in program_list:
    programs[program.code] = program


choice = 1
while choice != str(0):
    print("1. Add student\n2: Delete student\n3: Add program\n4: Delete program\n5: Add teacher\n8: Print student list\n9: Print program list\n0: Exit\n")
    choice = input("Enter option: ")
    if choice == str(1):
        #first create student object
        name = input("Enter the students name: ")
        age = input("Enter the students age: ")
        email = input("Enter the students email: ")
        personalnumber = input("Enter the students personal number: ")
        student = Student(name, age, email, personalnumber)
        
        #then add student to a program
        program_codes = input("Enter the students program(s)-code - enter multiple with ',': ").split(",")
        for code in program_codes:
            #using .upper() to match with program codes no matter the input style
            if code.upper() in programs:
                program = programs[code.upper()]
                student.enroll_student(program)
        students.append(student)
    elif choice == str(2):
        name = input("Enter student name you want to delete: ")
        for student in students:
            if student.name == name:
                students.remove(student)
    elif choice == str(3):
        pass
    elif choice == str(4):
        pass
    elif choice == str(5):
        pass
    elif choice == str(6):
        pers_num = input("Enter students personalnumber: ")
        for student in students:
            if student.personalnumber == pers_num:
                choice2 = ""
                while(choice2 != "x"):
                    print(student)
                    print("Change\na: Name\nb: Age\nc: Email\nd: Personalnumber\nExit: x")
                    choice2 = input("Enter option: ").lower()
                    if choice2 == "a":
                        student.name = input("Change name: ".format(student.name))
                    elif choice2 == "b":
                        student.age = input("Change age: ")
                    elif choice2 == "c":
                        student.email = input("Change email: ")
                    elif choice2 == "d":
                        student.personalnumber = input("Change personal number: ")
                    else:
                        pass
    elif choice == str(8):
        for student in students:
            print(student)
    elif choice == str(9):
        program_code = input("Enter the program code: ").upper()
        #if program exists, get thhe program object.
        if program_code in programs:
            program = programs[program_code]
            #add student values to a studentlist
            student_list = list(program.students.values())
            print("Students enrolled in program {}:".format(program_code))
            for student in student_list:
                print(student)
        else:
            print("Program {} not found.".format(program_code))

    else:
        pass
        
        