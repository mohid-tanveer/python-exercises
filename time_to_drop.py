# Exercise: Time to Drop

# Description:
# This very basic exercise will calculate the time to drop from a distance, planet radius, and planet mass 
# given by user.

import math

#declaration of gravity constant
gravity_constant = 6.674e-11
#prompt for user to input the distance and planet radius in meters along with the planet mass in kilograms
distance = float(input("From what height will the object be dropped in meters? "))
planet_radius = float(input("What is the radius of the planet you will be dropping the object on in meters? "))
planet_mass = float(input("What is the mass of the planet you will be dropping the object on in kilograms?"))

#prompt for user to input the object mass necessary to calculate gravitational force
object_mass = float(input("What is the mass of the object you will be dropping in kilograms?"))

#calculations of the time in seconds for the object to drop and its impact velocity
time_to_drop = math.sqrt(distance/(.5 * gravity_constant * (planet_mass / (planet_radius ** 2))))
object_velocity = (gravity_constant * (planet_mass / (planet_radius ** 2)) * time_to_drop)

#calculation for force at which the object strikes the planet
object_force = ((gravity_constant * planet_mass * object_mass) / (planet_radius ** 2))

#prints user's inputed data
print("\nDistance to drop (meters):", distance)
print("Radius of planet (meters): %.3e"%(planet_radius))
print("Mass of planet (kilograms): %.3e"%(planet_mass))
#prints calculated data of the time to drop, impact velocity, and force of object at impact
print("It will take", format(time_to_drop, '.4f'), "seconds for the object to drop", distance, "meters.")
print("The object will be traveling", format(object_velocity, '.4f'), "meters per second at impact and will strike the surface at", format(object_force, '.4f'), "Newtons of force.")

