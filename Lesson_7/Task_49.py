import math

def find_farthest_orbit(list_of_orbits):
    farthest_orbit = None
    max_distance = 0
 
    for orbit in list_of_orbits:
        a, b = orbit
        distance = math.sqrt(a**2 + b**2) # вычисляем расстояние от центра эллипса до фокуса
        if distance > max_distance:
            max_distance = distance
            farthest_orbit = orbit
   
    return farthest_orbit

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

