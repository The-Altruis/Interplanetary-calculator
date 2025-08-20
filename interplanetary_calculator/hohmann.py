import math
import csv
import check
import os
import time

def hohmann_transfer_calculator():
    #This is the hohmann calculator file.
    pi = math.pi
    planet_data = {}
    orbit_time = {}

    #This is a csv function. this opens the csv file and grabs the data needed
    def open_csv(solar_system):
        planet_data.clear()
        orbit_time.clear()

        script_dir = os.path.dirname(os.path.abspath(__file__))

        if solar_system == "kerbol system":
            filename = os.path.join(script_dir, 'kerbol_system.csv')
        elif solar_system == "sol system":
            filename = os.path.join(script_dir, 'solar_system')
        else:
            filename = os.path.join(script_dir, 'proxima_centarui.csv')
        with open(filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                name = row['Name'].strip().lower()
                semi_major_axis = float(row['Semi-major Axis (m)'])
                planet_data[name] = semi_major_axis
                orbital_period = float(row['Orbital Period (s)'])
                orbit_time[name] = orbital_period


    #This function is used to calculate the transfer angle window for two of the planets in the kerbol system.
    #I added a while loop due to the fact that when you put say,
    #Eeloo and kerbin, the output is less than -360, so I have it add 360,
    #till the out put is greater than -360.


    def hohmann_transfer_angles(location_axis, destination_axis, location_time,destination_time, GM):
        global number_of_orbits
        number_of_orbits = 0
        transfer_orbit = (location_axis + destination_axis) / 2
        travel_time = pi * math.sqrt((transfer_orbit)**3 / GM)
        angle_change = (travel_time / destination_time) * 360
        phase_angle = (180 - angle_change)
        while phase_angle < -360:
            phase_angle += 360
            number_of_orbits += 1
        print(f"Transfer Orbit Semi-major Axis: {transfer_orbit:.3e} m")
        print(f"Transfer Time: {travel_time:.3e} s")
        print(f"Origin Period: {location_time:.3e} s")
        print(f"Angle Change: {angle_change:.2f} degrees")
        print(f"Required Phase Angle: {phase_angle:.2f} degrees")
        return round(phase_angle)
    
    #This is used to calculate delta V for a transfer orbit
    #in order to calculate delta V, you need the gravitational parameter of the sun, the semi-major axis.
    #and the transfer orbit.

    def hohmann_delta_v_calculator(location_axis, destination_axis, GM):
        transfer_orbit = (location_axis + destination_axis) / 2
        delta_v1 = math.sqrt(GM * (2 / location_axis - 1 / transfer_orbit)) - math.sqrt((GM / location_axis))
        delta_v2 = math.sqrt(GM * (2 / destination_axis - 1 / transfer_orbit)) - math.sqrt((GM / destination_axis))
        delta_v_total = delta_v1 + delta_v2
        return round(delta_v_total)

    def time_calculator(semi_major_axis, GM):
        kepler_time = pi * math.sqrt((semi_major_axis)**3 / GM)
        kepler_time_days = kepler_time / 86400
        return round(kepler_time_days)

    #this is the info that is shown when running the program
    print("Interplanetary Hohmann Transfer Calculator for the Kerbin, Sol and Proxima Centauri systems:")
    print("---------------------------------------------------------")
    print("Kerbol System: Moho, Eve, Kerbin, Duna, Dres, Jool, Eeloo.")
    print("Solar System: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto.\n")

    #this is the user interface,
    #this asks the user for their current planet location and their desired location.
    #then it checks if what the user put in is the same, if it is, it ends the code and returns the user to the main screen.
    #if not it continues with the code.

    while True:
        solar_systems = input("are you in the Kerbol system, Sol system, or Proxima Centauri system? ").strip().lower()
        open_csv(solar_systems)
        print("Available planets:", ', '.join(planet_data.keys()))
        if solar_systems == "kerbol System":
            GM = 1.1723328e18
        elif solar_systems == "sol system":
            GM = 1.32712440018e20
        else:
            GM = 1.62e19
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
            print("Please wait...")
            print("------------------------------------------------------------")
            time.sleep(5)
        #this will go into the kerbol_system.csv file
        #and grab the semi-major axis and the orbital time for the planets

        location_axis = planet_data[location]
        destination_axis = planet_data[destination]
        location_time = orbit_time[location]
        destination_time = orbit_time[destination]
        check.more_efficient(location_axis, destination_axis)

        print(
            f"{location}: Axis = {location_axis:.3e}, Period = {location_time:.3e}"
        )
        print(
            f"{destination}: Axis = {destination_axis:.3e}, Period = {destination_time:.3e}"
        )

        print("Your Interplanetary transfer angle for " + str(location) + " and " +
            str(destination) + " is around " + str(hohmann_transfer_angles(location_axis, destination_axis, location_time, destination_time, GM)) + " degrees.")
        print("The delta V for " + str(location) + " and " + str(destination) + " is around " + str(hohmann_delta_v_calculator(location_axis, destination_axis, GM)) +" m/s")
        print("the number of orbits the target planet will have made is " + str(number_of_orbits))
        print("------------------------------------------------------------")
        calculate_time = input("Would you like to calculate the time it takes to get to " + str(destination) + "? ").capitalize()
        if calculate_time == "Yes":
            print(" ")
            print("the time it takes to get to " + str(destination) + " is " + str(time_calculator(location_axis, GM)) + " days.")
        print(" ")

        # this will restart to calculations and clear the console if you decide to continue so you don't have to scroll through hundreds of lines of console outputs
        redo_calculations = input(
            "Would you like to calculate something else? [Y/N] ").capitalize()
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