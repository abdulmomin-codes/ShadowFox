# 4. If Conditions Task
# 1. Write a program to determine the BMI Category based on user input.
# Ask the user to:
# Enter height in meters
# Enter weight in kilograms
# Calculate BMI using the formula: BMI = weight / (height)2
# Use the following categories:
# If BMI is 30 or greater, print "Obesity"
# If BMI is between 25 and 29, print "Overweight"
# If BMI is between 18.5 and 25, print "Normal"
# If BMI is less than 18.5, print "Underweight"
# Example:
# Enter height in meters: 1.75
# Enter weight in kilograms: 70
# Output: "Normal"
print("Question 1:")

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")
# 2. Write a program to determine which country a city belongs to. Given
# list of cities per country:
# Australia = ["Sydney","Melbourne","Brisbane","Perth"]
#  UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
# India = ["Mumbai","Bangalore","Chennai", "Delhi"]

# Ask the user to enter a city name and print the corresponding country.
# Example:
# Enter a city name: "Abu Dhabi"
# Output: "Abu Dhabi is in UAE"
print("\nQuestion 2:")

city = input("Enter a city name: ")

if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    print(f"{city} is in Australia")
elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    print(f"{city} is in UAE")
elif city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    print(f"{city} is in India")
else:
    print("City not found in the given list.")
# 3. Write a program to check if two cities belong to the same country.
# Ask the user to enter two cities and print whether they belong to the
# same country or not.

# Example:
# Enter the first city: "Mumbai"
# Enter the second city: "Chennai"
# Output: "Both cities are in India"
# Example:
# Enter the first city: "Sydney"
# Enter the second city: "Dubai"
# Output: "They don't belong to the same country"

print("\nQuestion 3:")

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in ["Sydney", "Melbourne", "Brisbane", "Perth"] and city2 in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    print("Both cities are in Australia")
elif city1 in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] and city2 in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    print("Both cities are in UAE")
elif city1 in ["Mumbai", "Bangalore", "Chennai", "Delhi"] and city2 in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")
