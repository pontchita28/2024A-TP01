# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Quel est le pourcentage de batterie? "))

distance = 0 
while 50 <battery_level <= 100:
    distance +=2
    battery_level -=1 
while 25 < battery_level <= 50:
    distance += 0.5
    battery_level -=1
while 10 < battery_level <= 25:
    distance += 1 
    battery_level -=1
while 5 < battery_level <= 10:
    distance += 2.5
    battery_level -= 1 
while 0 < battery_level <= 5 : 
    distance += 6 
    battery_level -=1
if battery_level == 0:
    print("La batterie est vide \n")

distance_round = round(distance, 1)
print(f"La distance possible est de {distance_round}km")
