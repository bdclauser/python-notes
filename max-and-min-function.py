# Takes any number of arguments and returns the largest one.
maximum = max(-5, -10, 5, 10, 20, 30, -500)

print(maximum)

# Takes an number of arguments and returns the smallest one.
minimum = min(-5, -10, 5, 10, 20, 30, -500)

print(minimum)

# Lets return the absolute value of a number using abs()
absolute = abs(-42)

print(absolute)

# Lets use type() to return the type of an argument

print(type(42))
print(type(4.2))
print(type('spam'))


# Review
def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"
