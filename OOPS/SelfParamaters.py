class Student:
    def studentDetails():
        # * this will require a parameter
        pass


# s1 = Student()
# s1.studentDetails()
# Student.studentDetails(s1)
# ? it is same as this --> class_name.function(object)


# Now making use of Self parameter
    
class Market:

    isGoodPercentage = 80

    def MarketThings(self):
        self.name = "Tomato" #* it is an instance attribute
        self.name = "Potato" #* instance variable
        self.price = 90
        print(self.name)
        print("Name = ", self.name)
        pass

    def isGood(self):
        if self.price > self.isGoodPercentage:
            print("The Market thing is good !!")
        else:
            print("The market thing is not good!!")
# s1 = Market()
# s1.MarketThings()

# s1.isGood()


# ! Predict the output
# what will be the output of this code

class Student_Class:
    name = "Kartik"

    def student_detail(self):
        self.age = 80
    
    def print_details(self):
        print(self.name, end=" ")
        print(self.age)

s = Student_Class()
s.student_detail()
s.print_details()