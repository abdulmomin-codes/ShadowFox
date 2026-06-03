# 6. Dictionary tasks
# 1. Create a list of your friends' names. The list should have at least 5 names.
# Create a list of tuples. Each tuple should contain a friend's name and the length
# of the name.
# For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)

print("Question 1:")

names = ["John", "Adam", "Sam", "Lily", "Eliza"]

name_and_length = []

for name in names:
    name_and_length.append((name, len(name)))

print("List of names and their lengths:")

for name, length in name_and_length:
    print(f"('{name}', {length})")

# 2.You and your partner are planning a trip, and you want to track expenses.
# Create two dictionaries, one for your expenses and one for your partner's
# expenses. Each dictionary should contain at least 5 expense categories and their
# corresponding amounts.
# For example:

print("\nQuestion 2:")

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate the total expenses for each of you and print the results.

total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())

print("Your total expenses:", total_your_expenses)
print("Partner's total expenses:", total_partner_expenses)

# Determine who spent more money overall and print the result.

if total_your_expenses > total_partner_expenses:
    print("You spent more money overall.")
elif total_partner_expenses > total_your_expenses:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount.")

# Find out the expense category where there is a significant difference in spending
# between you and your partner.

largest_difference = 0
significant_category = ""

for category in your_expenses:
    difference = abs(
        your_expenses[category] - partner_expenses[category]
    )

    if difference > largest_difference:
        largest_difference = difference
        significant_category = category
# Print the category and the difference.
print(
    f"The expense category with the largest difference is "
    f"'{significant_category}' with a difference of {largest_difference}."
)
