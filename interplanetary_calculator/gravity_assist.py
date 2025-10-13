import math

GM = 1.32712440018e20
R_earth = 6371000.0
R_mars = 3389500.0

nu_1 = math.radians(400)
e_1 = (R_earth - R_mars) / (R_earth + R_mars * math.cos(nu_1))
h_1 = math.sqrt(GM * R_earth * (1 - e_1))

V_p1 = h_1 / R_mars
V_r1 = GM / h_1 * e_1 * math.sin(nu_1)

