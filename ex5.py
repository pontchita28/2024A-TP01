#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = (input("Chaine représentant les médailles ? ")).upper()

# compter le nombre de lettres à chaque fois


if "G" in code_medals:
    number_g = code_medals.count("G")
elif "S" in code_medals:
    number_s = code_medals.count("S")
elif "B" in code_medals:
    number_b = code_medals.count("B")



print(f"Nombre de médailes: {number_g} or, \n\ {number_s} argent et {number_g} bronze")