import csv, os
from solar_system import SolarSystem

def load_solar_system(system_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_map = {
        "kerbol system": "kerbol_system.csv",
        "sol system": "solar_system.csv",
        "proxima centauri": "proxima centauri.csv"
    }

    if system_name not in file_map:
        raise ValueError(f"'{system_name}' not found in database.")
    
    filename = os.path.join(script_dir, file_map[system_name])

    GM_map = {
        "kerbol system": 1.1723328e18,
        "sol system": 1.32712440018e20,
        "proxima centauri": 1.62e19
    }

    system = SolarSystem(system_name, GM_map[system_name])

    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            system.add_planet(
                row['Name'],
                float(row['Semi-major Axis (m)']),
                float(row['Orbital Period (s)']),
                float(row['Mass (kg)']),
                float(row['Eccentricity']),
                float(row['Inclination (deg)']),
                float(row['GM (km^3/s^2)'])   
            )
    return system