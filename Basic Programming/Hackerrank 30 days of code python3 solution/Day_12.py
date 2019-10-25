#                      Name : Arif Khan
#                      Judge: HACKERRANK
#                      University: Primeasia University
#                      problem: Day 12: Inheritance
#                      Difficulty: Easy
#                      Problem Link: https://www.hackerrank.com/challenges/30-inheritance/problem
#

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        grades = 'OEAPDT'
        
        gradelist = [100 >= avg >= 90, 90 > avg >= 80, 80 > avg >= 70 , 70 > avg >= 55 , 55 > avg >= 40, 40 > avg]
        
        for i , m in zip(gradelist,grades):
            if i:
                return m

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())