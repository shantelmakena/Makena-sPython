# Datatype


number = 78  #Int
num = 45.09  #Float
greeting = " How are you doing"  # str
Is_Programming_Interesting = True  #bool
devices = ["laptop","computer","tablet","phone"]  # List
browsers = ("opera","firefox","safari","brave")   # Tuple
countries = {"Kenya","Uganda","Tanzania"}   # Set
employee = {
    "firstname" : "Jane",
    "age" : 29,
    "nationality" : "Kenyan",
    "emaailaddress" : "jane@gmail.com",
} # Dictionary




print(Is_Programming_Interesting)
print(num)
print(countries)
print(employee["firstname"])
print(employee["age"])


# Deatermining a datatype
print(type(countries))
print(type(employee))

# Typecasting is the process of converting one datatype to another
print(int(num))
print(float(number))