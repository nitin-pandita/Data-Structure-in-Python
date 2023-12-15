# Local variable
# ? Local variables are those variables that are declared inside the function

# Global Variables
# * Global variables are those variables that are declared outside the function


# Example of Local Variables
a1 = 10 # global variables as it is declared outside the function

def demoFun():
    a2 = 34 # it is local variable as it is declared inside the function
    print(a2)
# we can print the global variable easily like
print(a1)

# but we can't print the variable inside the function or we can't print the local variable

#* for printing the local variable we can call the function and then print it

demoFun()

a = 23
def printing():
    a = 12 # python will assume that we are creating a local variable as it is a global variable
    print(a)

print(a)
printing()
print(a) # will not change the value of the global variable as it is treating it as a local variable which is being declared inside the function