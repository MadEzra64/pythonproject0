# Declaring variables

# declaring how many cars
cars = 100

# declaring the space in a car
space_in_a_car = 4.0

# Declaring the amount of drivers
drivers = 30

# Declaring how many passengers
passengers = 90

# Declaring how many cars are not driven via math with variables. Cars subtracted from the amount of drivers.
cars_not_driven = cars - drivers

# Declaring the number of cars driven is equal to the number of drivers
cars_driven = drivers

# Declaring the capacity of the carpool multiplying the variables cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# Now we calculate the average passengers per car.
average_passengers_per_car = passengers / cars_driven

# Printing the declared variables within simple statements.
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
