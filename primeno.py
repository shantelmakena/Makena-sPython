# A python program that checks whether a number is prime or not
n1 = int(input("Enter number :"))

IS_PRIME = False

if n1 == 1:
    print("not prime")
elif n1 > 1:
    for i in range(2, n1):
        if (n1 % i) == 0:
            IS_PRIME = True
            break

if IS_PRIME:
      print("not prime")
else:
   print("is prime")