#EXCEPTIONS : these are the errors that occurs while executing the program
"""
Let's say we are traveling on road and if the road is clear this means there is no exception but if we see an accident
on that road this means we are having exception

"""

# Excepting Error
x = input("enter number: ")
y = input("enter number: ")
try:
    z = int(x)/int(y)
except Exception as e:
    print("Exceptions occured: ", e)
    z = None
print('Result is ', z)

#Excepting Specific Type of error

num1 = input('Num1 :')
num2 = input('Num2 :')

try:
    divi = int(num1) / int(num2)
except ZeroDivisionError as e:
    print('ZeroExceptioneroor occured')
    divi = None
print('Result is ', divi)


#excepying multiple Exceptions

num1 = input('Num1 :')
num2 = input('Num2 :')

try:
    divi = (num1) / int(num2)
except ZeroDivisionError as e:
    print('ZeroExceptioneroor occured')
    divi = None
except Exception as e:
    print('Exception type is ', type(e).__name__)
    divi = None
print('Result is ', divi)