# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

import math 

g = 9.8
speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancé (en degrés): "))

max_dist = round((((speed ** 2) * math.sin (math.radians(2 * angle)))/g),2)

print(f"Distance parcourue: {max_dist}m")

