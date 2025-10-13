from data_loader import load_solar_system
import math

def hohmann_transfer_calculator():
    #This is the hohmann calculator file.
    pi = math.pi

    system_name = input("Which solar system are you in? ").strip().lower()
    system = load_solar_system(system_name)

    # access planets
    print("Available planets:", ', '.join(system.planets.keys()))

    location = input("What planet are you on? ").strip().lower()
    destination = input("What planet do you want to go to? ").strip().lower()

    if location == destination:
        print("Your location and destination cannot be the same.")
        return

    if location not in system.planets or destination not in system.planets:
        print("Invalid planet.")
        return

    location_axis = system.get_planet(location)["axis"]
    destination_axis = system.get_planet(destination)["axis"]
    location_time = system.get_planet(location)["orbital_period"]
    destination_time = system.get_planet(destination)["orbital_period"]



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
    print("Proxima Centarui: Proxima Centarui b, Proxima Centarui d, Proxima Centauri c (candidate).\n")

    #this is the user interface,
    #this asks the user for their current planet location and their desired location.
    #then it checks if what the user put in is the same, if it is, it ends the code and returns the user to the main screen.
    #if not it continues with the code.

    system = load_solar_system(system_name)
    GM = system.GM_star

    while True:

        if location == destination:
            print("Location and destination cannot be the same.")
            break
        if location not in system.planets or destination not in system.planets:
            print("Invalid planet.")
            break

        location_axis = system.get_planet(location)["axis"]
        destination_axis = system.get_planet(destination)["axis"]
        location_time = system.get_planet(location)["orbital_period"]
        destination_time = system.get_planet(destination)["orbital_period"]

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
        redo_calculations = input("Would you like to calculate something else? [Y/N] ").lower()
        if redo_calculations in ["y", "yes"]:
            print("------------------------------------------------------------")
            print(" ")
            continue
        elif redo_calculations in ["n", "no"]:
            print(" ")
            print("Understood. Enjoy your day.")
            break
        else:
            print(" ")
            print("I'm sorry, that is not a suitable answer.")
            break