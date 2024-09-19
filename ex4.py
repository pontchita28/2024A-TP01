# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

import math 

battery_level = (float(input("Pourcentage de batterie ? ")))
distance = 0


if battery_level == 0:
    print("La batterie est vide")
else:
    if 50 <battery_level <= 100:
        distance = 2*(battery_level - 50)
        battery_level -= battery_level - 50
    if 25 < battery_level <= 50:
        distance += 0.5*(battery_level - 25)
        battery_level -=  battery_level - 25
    if 10 < battery_level <= 25:
        distance += 1 *(battery_level - 10)
        battery_level -= battery_level - 10
    if 5 < battery_level <= 10:
        distance += 2.5*(battery_level - 5)
        battery_level -= battery_level - 5 
    if 0 < battery_level <= 5 : 
        distance += 6*(battery_level)



distance_round = round((distance),1)
if distance > 0:
    print(f"{distance_round} km")




