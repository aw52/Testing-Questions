import random  # this is the randomizer module
import sys # this is for changing the output location (for the file)
protein = ['Beef','Steak Strip','Chicken','Turkey','Pork',]
starch = ['Rice Bowl','Risotto','Pasta',]
veggies = ['Broccoli','Carrots','Brussels Sprouts','Spinach','Corn','Asparagus','Tomato','Zucchini','Onion','Potatoes',]
other_ingredients = ['Mushrooms','Cheese','Breading','Salad','Peanuts','Bacon', 'Walnuts', 'Pecans',]
characteristics = ['Spicy','BBQ', 'Sweet', 'Savory',]

def random_protein():
    return(random.choice(protein))
protein = random_protein()
def random_starch():
    return(random.choice(starch))
starch = random_starch()
def random_veggies():
    return(random.choice(veggies))
veggies = random_veggies()
def random_other_ingredients():
    return(random.choice(other_ingredients))
other_ingredients = random_other_ingredients()
def random_characteristics():
    return(random.choice(characteristics))
characteristics = random_characteristics()

def random_recipe():
    print(str(characteristics), str(protein),  str(starch), "with", str(veggies), "and", str(other_ingredients))

outfile = open('Randomized Recipe.txt', 'w+')
terminal_output = sys.stdout

print("Here's your random recipes:", file=outfile)
sys.stdout = outfile
quantity = 5
random_recipe()
sys.stdout = terminal_output
print("Your recipes have been saved!")