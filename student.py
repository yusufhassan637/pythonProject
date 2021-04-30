from user import User
from user import User

class Student(User):
    result = 0
    def type(self):

     student_essay = input("Hello Student. \nPlease type your essay")

     self.calulate(self, student_essay)
     e1 = Essay()

     e1.sentence = len(student_essay.split(".")) - 1

     e1.world = len(student_essay.split("."))

     self.result



    def display(self):
        print("Average number of words in your eassy is:" + str(self.result))