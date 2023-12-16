import os


# creation d une liste contenant les noms des fichiers
def list_of_files(directory, extension):
    """
    Permet de récupérer la liste des noms des fichiers contenus dans un dossier. On s'intéressera ici à 'speeches'
    :param directory:
    :param extension:
    :return: files_names
    """
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# creation des doubles des fichiers + copie du contenu en miniscule sans ponctuation
def copie(L):
    """
    Permet de mettre les fichiers sous le bon format : tout en minuscule sans ponctuation et les range dans un nouveau dossier appelé cleaned
    :param L: liste
    :return:
    """
    for i in range(len(L)):
        fichier = open("cleaned/" + L[i], "w")
        with open("speeches/" + L[i]) as files:
            for line in files:
                for char in line:
                    if 64 < ord(char) < 91:
                        fichier.write(chr(ord(char) + 32))
                    elif char == ":" or char == "." or char == "!" or char == "?" or char == "," or char == ";" or char == chr(
                            34):
                        fichier.write("")
                    elif char == "-" or char == "'":
                        fichier.write(" ")
                    else:
                        fichier.write(char)
        fichier.close()


# extraction des noms des presidents+ affichage des noms
def president_names(L, A):
    """
    Crée une liste contenant tous les noms des présidents contenus dans speeches
    :param L: liste
    :param A: liste
    :return:
    """
    b = 0
    for i in range(len(L)):
        if "2" not in L[i]:
            A.append(L[i][11:-4])
            if "1" in A[b]:
                A[b] = A[b][:-1]
            b += 1