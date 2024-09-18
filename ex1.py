# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom: ")
date = input("Date du record? ")
discipline = input("Dans quelle discipline ? ")
category = input("Dans quelle catégorie spécifique ? ")
record = input("Quel est le record ? ")

# ajouter des \n \ pour indiquer que le reste du str se
# trouve sur la prochaine ligne
print(f"Nouveau Record: \n\
-------------------- \n \
{date} - {discipline} - {category}: \n\
        {athlete} - {record}")