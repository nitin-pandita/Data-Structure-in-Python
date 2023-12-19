class StaticMethod:
    @staticmethod
    # ? we use static method to remove the use of self in the function
    def WelcomeToSchool():
        print("Welcome to College Students")


s1 = StaticMethod()
s1.WelcomeToSchool()