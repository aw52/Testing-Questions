import random 
import sys
outfile = open('Randomized Recipe.txt', 'w+')
terminal_output = sys.stdout
print("Here's your random recipes:", file=outfile)
sys.stdout = outfile

protein = ['Beef','Steak Strip','Chicken','Turkey','Pork',]
starch = ['Rice Bowl','Risotto','Pasta',]
veggies = ['Broccoli','Carrots','Brussels Sprouts','Spinach','Corn','Asparagus','Tomato','Zucchini','Onion','Potatoes',]
other_ingredients = ['Mushrooms','Cheese','Breading','Salad','Peanuts','Bacon', 'Walnuts', 'Pecans',]
characteristics = ['Spicy','BBQ', 'Sweet', 'Savory',]

def randomize():
    print(random.choice(characteristics), random.choice(protein), random.choice(starch), "with", random.choice(veggies), "and",random.choice(other_ingredients))

y = 5
x = 0
while x < y:
    print(random.choice(characteristics), random.choice(protein), random.choice(starch), "with", random.choice(veggies), "and",random.choice(other_ingredients))
    x += 1

sys.stdout = terminal_output
print("Your recipes have been saved!")
