class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.attend = 0
        self.marks = []
        print("Welcome {} to Havard high school" .format(name))


    def addmarks(self, ma):
        self.marks.append(ma)

    def attendays(self):
        self.attend += 1

    def getavg(self):
        return sum(self.marks) / len(self.marks)

    def attavg(self):
        return sum(self.attend) / len(self.attend)

    def classbell(self):
        print("Ring the class bell")

    def gohome(self):
        print('Time to go home, school has ended')
        
