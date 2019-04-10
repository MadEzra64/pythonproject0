name = 'Adam Zupancic'
age = 35 # as of today
height = 74 # inches
weight = 180 # pounds
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'
cent_height = 0
kilo_weight = 0

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy")
print("That's actually not to bad.")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} unless he drank coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print("Now let's do some basic metric conversions in python...")

cent_height = height * 2.54

print(f"{height} inches converts to {cent_height}.")

print("Now we convert pounds to kilograms.")

kilo_weight = weight / 2.205

print(f"{weight}lbs converts to {kilo_weight}kg.")
print(round(kilo_weight))
