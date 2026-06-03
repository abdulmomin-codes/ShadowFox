# List Task
#You have a list of superheroes representing the Justice
# League. 
# justice_league = ["Superman","Batman", "WonderWoman","Flash","Aquaman","Green Lantern"]
# Perform the following tasks:
# Question 1. Calculate the number of members in the Justice League.
print("Question 1:")

justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Number of members in the Justice League:", len(justice_league))
print("Justice League members:", justice_league)

# Question 2
# Batman recruited Batgirl and Nightwing as new members.
# Add them to your list.

print("\nQuestion 2:")

justice_league.extend(["Batgirl", "Nightwing"])

print("Justice League members:", justice_league)

# Question 3
#Wonder Woman is now the leader of the Justice League.
# Move her to the beginning of the list.

print("\nQuestion 3:")

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("Justice League members:", justice_league)

# Question 4
#  Aquaman and Flash are having conflicts, and you need to
# separate them. Choose either "Green Lantern" or "Superman"
# and move them in between Aquaman and Flash.

print("\nQuestion 4:")

justice_league.remove("Green Lantern")
justice_league.insert(4, "Green Lantern")

print("Justice League members:", justice_league)

# Question 5
# The Justice League faced a crisis, and Superman decided to
# assemble a new team. Replace the existing list with the following
# new members: "Cyborg","Shazam","Hawkgirl","MartianManhunter","Green Arrow".

print("\nQuestion 5:")

justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("New Justice League:", justice_league)

#  Question 6
# Sort the Justice League alphabetically. The hero at the 0th
# index will become the new leader.
# (BONUS: Can you predict who the new leader will be?)

# Your task is to write Python code to perform these operations on
# the "justice_league" list. Display the list at each step to observe
# the changes.
print("\nQuestion 6:")

justice_league.sort()

print("Sorted Justice League:", justice_league)
print("New leader of the Justice League:", justice_league[0])
