# VARIABLES TASK

# Question 1:
# Create a variable named pi and store the value 22/7 in it.
# Now check the data type of this variable.

pi = 22/7
print("Question 1")
print("Data type of pi:", type(pi))


# Question 2:
# Create a variable called for and assign it a value 4. See what
# happens and find out the reason behind the behavior that you
# see.

print("\nQuestion 2")
print("'for' is a reserved keyword in Python.")
# Reason: Cannot create variable 'for' because 'for' is a reserved keyword in Python.
# Example:
# for = 4
# SyntaxError


# Question 3:
# Store the principal amount, rate of interest, and time in
# different variables and then calculate the Simple Interest for 3
# years. Formula: Simple Interest = P x R x T / 100

print("\nQuestion 3")

principal_amount = 1000
rate_of_interest = 5
time = 3

simple_interest = (principal_amount * rate_of_interest * time) / 100

print("Simple Interest =", simple_interest)
