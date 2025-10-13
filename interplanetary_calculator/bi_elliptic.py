from data_loader import load_solar_system
import math

def bi_elliptic_transfer_calculator():
    print("Interplanetary Bi-elliptic Transfer Calculator for the Kerbin and Sol systems:")
    pi = math.pi
    system_name = input("Which solar system are you in? ").strip().lower()
    system = load_solar_system(system_name)
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

    #this just defines a_1 and a_2 semi-major axis'. it uses the two orbits, the inital and final orbits. and r_b as whatever parameter is inputed. Though, I wouldn't reccomend this transfer to get from planet-to-planet. only LEO and HEO, or any low and high orbit for a planet.
    def bi_elliptic_transfer(location_axis, destination_axis, r_b):
        a_1 = (location_axis + r_b) / 2
        a_2 = (destination_axis + r_b) / 2
        return a_1, a_2
        """  
        In this function, I had set GM to be the gravitational parameter. a_1 and a_2 are the half orbits of the two elliptical orbits for this transfer.
        While they are mor commonly known as Semi-major axis of the two transfer orbits. I just used the mathmatical symbols for them. now, r_b is whatever parameter the user inputs, I would reccomend 3e11 or 4e11. (the computer knows what it is.)
        """
    def bi_elliptic_dv(location_axis, destination_axis, r_b, GM, a_1, a_2):
        dv1 = math.sqrt(2 * GM / location_axis - GM / a_1) - math.sqrt(GM / location_axis)
        dv2 = math.sqrt(2 * GM / r_b - GM / a_2) - math.sqrt(2 * GM / r_b - GM / a_1)
        dv3 = math.sqrt(2 * GM / destination_axis - GM / a_2) - math.sqrt(GM / destination_axis)
        total_dv = abs(dv1) + abs(dv2) + abs(dv3)
        return dv1, dv2, dv3, total_dv
        """
        Now, the transfer time equationb is a bit tricky, and I'm gonna explain why. in the wiki article and in reports on the Bi-elliptic transfer, there is a T = 2pi * (math.sqrt(a ** 3 / GM)). for those who don't know, a is either a_1 or a_2, but it's the full orbit
        not the half orbit. this, calculates the time it takes to complete the FULL orbit of a_1 or a_2. and in this instance, that's not helpful so you have to use t1 = (pi * math.sqrt(a_1 ** 3 / GM)) / 86400 and t2 = (pi * math.sqrt(a_2 ** 3 / GM)) / 86400.
        Why you may ask? because they take the HALF elliptical orbits of a_1 and a_2 to find the time for HALF or those orbits, then you add them and you get the full transfer time.
        """
    def bi_elliptic_time(a_1, a_2, GM):
        t1 = (pi * math.sqrt(a_1 ** 3 / GM)) / 86400
        t2 = (pi * math.sqrt(a_2 ** 3 / GM)) / 86400
        e_total = t1 + t2
        return t1, t2, e_total
    
    #this is going to be shown when you start up this file for the calculator and it'll show you the avaliable planets and which calculator you're using.



    system = load_solar_system(system_name)
    GM = system.GM_star

    while True:
            r_b = float(input("Enter your chosen apoapsis radius (r_b) in meters: "))
            if location == destination:
                print("Location and destination cannot be the same.")
                break
            if location not in system.planets or destination not in system.planets:
                print("Invalid planet.")
                break
            
            location_axis = system.get_planet(location)["axis"]
            destination_axis = system.get_planet(destination)["axis"]

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
                
            redo_calculations = input("Would you like to calculate something else? [Y/N] ").strip().lower()
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