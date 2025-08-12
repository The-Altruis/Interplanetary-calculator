import math
import csv
import check
import os
import time
def bi_elliptic_transfer_calculator():
  
  pi = math.pi
  planet_data = {}
  
  def open_csv(solar_system):
    planet_data.clear()

    script_dir = os.path.dirname(os.path.abspath(__file__))

    if solar_system == "yes":
        filename = os.path.join(script_dir, 'kerbol_system.csv')
    else:
        filename = os.path.join(script_dir, 'solar_system.csv')
    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            name = row['Name'].strip().lower()
            semi_major_axis = float(row['Semi-major Axis (m)'])
            planet_data[name] = semi_major_axis
  
  def bi_elliptic_transfer(location_axis, destination_axis, r_b):
    a_1 = (location_axis + r_b) / 2
    a_2 = (destination_axis + r_b) / 2
    return a_1, a_2
  

  def bi_elliptic_dv(location_axis, destination_axis, r_b, GM, a_1, a_2):
    dv1 = math.sqrt(2 * GM / location_axis - GM / a_1) - math.sqrt(GM / location_axis)
    dv2 = math.sqrt(2 * GM / r_b - GM / a_2) - math.sqrt(2 * GM / r_b - GM / a_1)
    dv3 = math.sqrt(2 * GM / destination_axis - GM / a_2) - math.sqrt(GM / destination_axis)
    total_dv = abs(dv1) + abs(dv2) + abs(dv3)
    return dv1, dv2, dv3, total_dv
  
  def bi_elliptic_time(a_1, a_2, GM):
    t1 = (pi * math.sqrt(a_1 ** 3 / GM)) / 86400
    t2 = (pi * math.sqrt(a_2 ** 3 / GM)) / 86400
    e_total = t1 + t2
    return t1, t2, e_total
  
  while True:
    #this is going to be shown when you start up this file for the calculator
    print("Interplanetary Bi-elliptic Transfer Calculator for the Kerbin and Sol systems:")
    print("---------------------------------------------------------")
    print("Kerbol System: Moho, Eve, Kerbin, Duna, Dres, Jool, Eeloo.")
    print("Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto.\n")

    solar_systems = input("are you in the kerbol System? ").strip().lower()
    open_csv(solar_systems)
    print("Available planets:", ', '.join(planet_data.keys()))
    if solar_systems == "yes":
        GM = 1.1723328e18
    else:
        GM = 1.32712440018e20
    print(" ")
    location = input("what planet are you on? ").strip().lower()
    print(" ")
    destination = input("What planet do you want to go to? ").strip().lower()
    if location == destination:
        print(" ")
        print("Your location and destination cannot be the same. Shutting off...")
        break
    elif location not in planet_data or destination not in planet_data:
        print(" ")
        print("Your input contains a Planet that is not in the Kerbol Solar System or in our Solar System.")
        break
    else:
        print(" ")
        r_b = float(input("Enter your chosen apoapsis radius (r_b) in meters: "))
        print(" ")
        print("Please wait...")
        print("------------------------------------------------------------")
        time.sleep(5)
    location_axis = planet_data[location]
    destination_axis = planet_data[destination]
    check.more_efficient(location_axis, destination_axis)

    a_1, a_2 = bi_elliptic_transfer(location_axis, destination_axis, r_b)
    t1, t2, t_total = bi_elliptic_time(a_1, a_2, GM)
    dv1, dv2, dv3, total_dv = bi_elliptic_dv(location_axis, destination_axis, r_b, GM, a_1, a_2)
    print(f"{location.capitalize()}: Axis = {location_axis:.3e}")
    print(f"{destination.capitalize()}: Axis = {destination_axis:.3e}")
    print(f"a₁ (from {location.capitalize()} to r_b): {a_1:.2e} m")
    print(f"a₂ (from r_b to {destination.capitalize()}): {a_2:.2e} m")
    print(f"the amount of time from {location.capitalize()} to r_b is {t1:.2f} days")
    print(f"then the amount of time from r_b to {destination.capitalize()} is {t2:.2f} days")
    print(f"In total, the amount of time it'd take from {location.capitalize()} to {destination.capitalize()} is {t_total:.2f} days")
    print(f"To start the a₁ orbit, you need a delta v of {dv1:.2f} m/s")
    print(f"To go from a₁ to a₂, you'll need a delta v of {dv2:.2f} m/s")
    print(f"Then to exit the a₂ orbit, you'll need a delta v of {dv3:.2f} m/s")
    print(f"In total, you'll need a max delta v of {total_dv:.2f} m/s")
    print("------------------------------------------------------------\n")
        
    redo_calculations = input("Would you like to calculate something else? [Y/N] ").capitalize()
    if redo_calculations == "Yes":
        print("------------------------------------------------------------")
        print(" ")
        continue
    elif redo_calculations == "No":
        print(" ")
        print("Understood. Enjoy your day.")
        break
    else:
        print(" ")
        print("I'm sorry, that is not a suitable answer.")
        break