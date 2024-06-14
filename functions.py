# Inbuilt Functions/Standard Library Functions

y = min(23, 56, 1000, 5647)
print(y)


x = max(90, 2, 76, 14)
print("the maximum number is", x)



z = pow(2, 3)
print(z)


# User defined functions
def school():
    print("eMobilis")
school() # Calling a function


def multiply():
    num1 = 5
    num2 = 6
    print(num1 * num2)
multiply()


# Parameters and arguments
def add(a, b):
    print(a + b)
add( 5, 6)
add( 10, 2)
add( 56, 78)
add( 90, 50)


def Employee(fullname,age,salary,phoneno,position):
    print(fullname,age,salary,phoneno,position)

Employee("Job Kamau",45,500000,745689023,"MD")
Employee("Keisha Wanyoike",42,500000,790865412,"Admin")
Employee("Sarah Adeya",40,500000,778654034,"Secretary")
Employee("Charles Ndambuki",54,1000000,709854389,"CEO")

