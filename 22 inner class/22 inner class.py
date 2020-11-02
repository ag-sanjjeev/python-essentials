# inner class or class inside another class
class school:
    def __init__(self, standard, section):
        self.standard = standard
        self.section = section
        self.stu = self.student  # creating instance for inner class

    def show(self):
        print(self.standard, self.section)

    class student:
        def __init__(self, name, rollno):
            self.name = name
            self.rollno = rollno

        def show(self):
            print(self.name, self.rollno)


sc1 = school('2', 'A')
sc2 = school('3', 'B')

sc1.show()
sc2.show()

st1 = sc1.student('san', 42)  # creating object for inner class
st2 = sc2.student('velan', 50)

st1.show()
st2.show()