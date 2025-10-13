import math as m
from data_loader import load_solar_system

pi = m.pi

system_name = input("Which solar system are you in? ").strip().lower()
system = load_solar_system(system_name)
print("Available planets:", ', '.join(system.planets.keys()))

location = input("What planet are you on? ").strip().lower()
destination = input("What planet do you want to go to? ").strip().lower()

if location == destination:
    raise ValueError("Your location and destination cannot be the same.")

if location not in system.planets or destination not in system.planets:
    raise ValueError("Invalid planet name.")

GM = system.GM_star
AU = 1.496e8
r1 = system.get_planet(location)["axis"] * AU
r2 = system.get_planet(destination)["axis"] * AU
GM_dest = system.get_planet(destination)["GM"] / 1e9

e_1 = abs(r1 - r2) / (r1 + r2)

h_1 = m.sqrt(GM * r1 * (1 - e_1**2))

nu_1 = m.radians(float(input("Enter true anomaly (0-360): ")))
 
V_p1 = h_1 / r1
V_r1 = (GM / h_1) * e_1 * m.sin(nu_1)
V_1 = m.sqrt(V_p1**2 + V_r1**2)
alpha_1 = m.degrees(m.atan2(V_r1, V_p1))

V_planet = m.sqrt(GM / r2)

v_infty1_V = V_p1 - V_planet
v_infty1_S = -V_r1
v_infty = m.sqrt(v_infty1_V**2 + v_infty1_S**2)

r_p = 300 + 6378
e_hyp = 1 + (r_p * v_infty**2) / GM_dest
delta = 2 * m.asin(1 / e_hyp)

phi_1 = m.atan2(v_infty1_S, v_infty1_V)
phi_2_leading = phi_1 + delta
phi_2_trailing = phi_1 - delta

print(f"Incoming flight path angle (φ₁): {m.degrees(phi_1):.2f}°")
print(f"Leading trajectory angle (φ₂₊): {m.degrees(phi_2_leading):.2f}°")
print(f"Trailing trajectory angle (φ₂₋): {m.degrees(phi_2_trailing):.2f}°")
print(f"Deflection angle (δ): {m.degrees(delta):.2f}°")
print(f"Hyperbolic excess velocity (v∞): {v_infty:.3f} km/s")
