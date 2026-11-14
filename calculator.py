import math
def sum(a, b):
    return a + b
def substract(a,b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def sine(angle):
    return math.sin(math.radians(angle))
def cosine(angle):
    return math.cos(math.radians(angle))
def tangent(angle):
    return math.tan(math.radians(angle))
def exponential(x):
    return math.exp(x)
def logarithm(x):
    if x <= 0:
        raise ValueError("x must be positive value")
    return math.log(x)
