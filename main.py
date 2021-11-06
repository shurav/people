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
a = People("Sam", 0)
a.citizenship(0)
a.display()