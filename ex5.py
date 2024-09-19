#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ?")
code_medals = (input(" Chaine représentant les médailles ? ")).upper()

# compter le nombre de lettres à chaque fois


# compter le nombre de médailles dans la chaîne
number_g = code_medals.count("G")
number_s = code_medals.count("S")
number_b = code_medals.count("B")

total = number_g + number_s + number_b



if total != len(code_medals):
    # si le total n'est pas égal à la longueur de la chaîne
    # retourner que ce n'est pas une chaîne valide 
    print("Ceci est une chaine invalide.")
else:
    # sinon, retouurner le résultat directement 
    print(f"{country}:\n- {number_g} Or\n- {number_s} Argent\n- {number_g} Bronze")