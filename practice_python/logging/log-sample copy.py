import logging


# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# Warning: An indication that something unexpected happened,or indicative of some problem 
#           in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename='test.log', level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

num1 = 200
num2 = 100

add_result = add(num1, num2)
logging.debug(f"Add: {num1} + {num2} = {add_result}")

sub_result = sub(num1, num2)
logging.debug(f"Subtract: {num1} - {num2} = {sub_result}")

mult_result = mult(num1, num2)
logging.debug(f"Multiply: {num1} * {num2} = {mult_result}")

div_result = div(num1, num2)
logging.debug(f"Divide: {num1} / {num2} = {div_result}")