# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math 
water_quantity = input("Quelle quantité d'eau faut-il assainir? ")
water_quantity_int = float(water_quantity)

# calcul du filtre 
    # besoin de 1 filtre par 5L d'eau
filtre = math.ceil(1 * (water_quantity_int / 5))

# calcul des lampes UV 
    # besoin de 3 lampes UV par 5 L d'eau
uv = math.ceil(3 * (water_quantity_int / 5))

# calcul du Cl
    # besoin de 0.5 kg par 5 L
cl = round(0.5 * (water_quantity_int / 5), 1)

print(f"Voici les matériaux requis pour l'assainissement de {water_quantity_int}L d'eau: \n\
        - Filtres: {filtre} \n\
        - Lampes UV: {uv}  \n\
        - Chlore UV : {cl}")
