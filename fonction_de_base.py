import os


# creation d une liste contenant les noms des fichiers
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# cretion des doubles des fichiers + copie du contenu en miniscule sans ponctuation
def copie(L):
    for i in range(len(L)):
        fichier = open("cleaned/" + L[i], "w")
        with open("speeches/" + L[i]) as files:
            for line in files:
                for char in line:
                    if 64 < ord(char) < 91:
                        fichier.write(chr(ord(char) + 32))
                    elif char == ":" or char == "." or char == "!" or char == "?" or char == "," or char == ";":
                        fichier.write("")
                    elif char == "-" or char == "'":
                        fichier.write(" ")
                    else:
                        fichier.write(char)
        fichier.close()


# extraction des noms des presidents+ affichage des noms
def president_names(L, A):
    b = 0
    for i in range(len(L)):
        if "2" not in L[i] :
            A.append(L[i][11:-4])
            if "1" in A[b]:
                A[b] = A[b][:-1]
            b += 1




