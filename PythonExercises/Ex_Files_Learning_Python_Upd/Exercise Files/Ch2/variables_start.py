# 
# Example file for variables
#

# Declare a variable and initialize it
n=0
# print(n)


# re-declaring the variable works
# n="Nya"
# print(n)



# ERROR: variables of different types cannot be combined
# print("This is a string " + str(123))



# Global vs. local variables in functions
def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)
