T = float(input("Enter the time"))
f = 15
r = 5
h = 10
vol_of_tank = 3.14 * r ** 2 * h
vol_of_water = f * T
H = (vol_of_tank - vol_of_water)/(3.14 * r ** 2)
V =  vol_of_water - vol_of_tank
if vol_of_tank > vol_of_water:
    print(f"The  tank is underflow with remaning height {H} m")
elif vol_of_tank < vol_of_water:
    print(f"The tank is overflowed and {V} m**3 vol. of water is wasted")
else:
    print("The tank is filled")
