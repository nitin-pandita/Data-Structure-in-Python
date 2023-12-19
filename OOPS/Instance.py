class Student:
    pass

s1 = Student()
s2 = Student()
s3 = Student()


s1.name = "Nitin"

s2.name = "Kartik"
s2.RollNo = 23

s3.name = "Rohan"
s3.RollNo = 12

print(s2.__dict__)