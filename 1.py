"""Create a program that asks
the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old."""

name = input('Enter your name')
age = int(input('Enter your age'))
years = 100-age
print(f'Hi {name} you will turn 100 in {years} years')

# Extra
printNo = int(input('How many time do you want to print the text'))
print(f'Hi {name} you will turn 100 in {years} years\n' * printNo)
