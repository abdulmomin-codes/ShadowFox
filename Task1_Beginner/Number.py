#Numbers Task
# # Question 1. Write a function that takes two arguments, 145 and 'o'
# , and
# uses the `format` function to return a formatted string. Print the
# result. Try to identify the representation used.

print("Question 1:")

def number(num, alphabet):
    return format(num, alphabet)

result = number(145, 'o')

print("Output:", result)
# Reason: 'o' represents octal (base 8) format.

# Question 2
# In a village, there is a circular pond with a radius of 84 meters.
# Calculate the area of the pond using the formula: Circle Area = π
# r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
# 1.4 liters of water in a square meter, what is the total amount of
# water in the pond? Print the answer without any decimal point in
# it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
# Water per Square Meter

print("\nQuestion 2:")

radius = 84
pi = 3.14

area = pi * (radius ** 2)
print("Area of the pond:", int(area), "square meters")

water_per_square_meter = 1.4
total_water = area * water_per_square_meter

print("Total water in the pond:", int(total_water), "liters")

# Question 3
# 3. If you cross a 490meterlong street in 7 minutes, calculate your
# speed in meters per second. Print the answer without any decimal
# point in it. Hint: Speed = Distance / Time
print("\nQuestion 3:")

distance = 490
time = 7 * 60

speed = distance / time

print("Speed:", int(speed), "meters per second")
