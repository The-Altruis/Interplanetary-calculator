class SolarSystem:
    def __init__(self, name, GM_star):
        self.name = name
        self.GM_star = GM_star
        self.planets = {}

    def add_planet(self, name, semi_major_axis, orbital_period, mass=None, ecc=None, incl=None, GM=None):
        self.planets[name.lower()] = {
            "axis": semi_major_axis,
            "orbital_period": orbital_period,
            "mass": mass,
            "eccentricity": ecc,
            "inclination": incl,
            "GM": GM
        }

    def get_planet(self, name):
        return self.planets[name.lower()]
