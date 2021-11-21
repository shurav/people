class People:
    def __init__(self, name, ssn):
        while True:
            try:
                ssn = str(ssn)
                if(ssn == "0"):
                    self.name = name
                    self.ssn = None
                while((len(ssn) != 9 or not ssn.isdigit()) and ssn != "0"):
                    ssn = input("Enter a valid ssn: ")
                self.name = name
                self.ssn = ssn
            except ValueError:
                print("invalid input")
            else:
                break
    def citizenship(self, status):
        if(status == True):
            self.citizen = True
        else:
            self.citizen = False
    def display(self):
        print(self.name, '\n', self.ssn, '\n', "Citizenship: ", self.citizen)

class Student(People):
    def __init__(self, name, ssn, ID, year):
        self.ID = ID
        self.year = year
        People.__init__(self, name, ssn)
    def classes(self):
        classList = []
        className = None
        stop = "2"
        print("Enter the list of clases you are taking (Enter '0' when finished): ")
        while(stop != "0"):
            className = input("Enter the class: ")
            classList.append(className)
            stop = input("Want to keep adding more classes? (Enter 'o' if not): ")
            self.classList = classList
        return classList
    def display(self):
        People.display(self)
        print("Student ID:", self.ID, '\n', "Year:", self.year, '\n', "Classes: ", self.classList)
a = People("Sam", 0)
a.citizenship(0)
a.display()
b = Student("Jake", 781891871, "222", "sr")
b.citizenship(1)
b.classes()
b.display()
