from fonction_de_base import *
from TF_IDF import *
from fonctionnalites import *
from chatbot import *

president = []
president_avec_numero = []

# création du dictionnaire contenant les noms et prenoms des presidents
dictionnaire_nom_president = {
    "Giscard dEstaing": "Valéry",
    "Hollande": "François",
    "Macron": "Emmanuel",
    "Chirac": "Jacques",
    "Mitterrand": "François",
    "Sarkozy": "Nicolas"
}

if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    copie(files_names)
    president_names(files_names, president)
    president_names_fichier(files_names, president_avec_numero)
    occurence_president = dico_mot_presidents(president_avec_numero)
    occurence_president_2 = dico_mot_presidents(president_avec_numero)
    TF1 = TF(occurence_president, files_names, president_avec_numero)

    IDFdict = IDF(TF1)
    TFIDF = TF_IDF(TF1, IDFdict, )

    print(" appuyez sur 1 pour utiliser le chat bot\n"
          , "appuyez sur 2 pour utiliser les fonctions prédéfinies")
    chatbot_ou_predefini = int(input())
    while not(1 <= chatbot_ou_predefini <= 2):
        print(" appuyez sur 1 pour utiliser le chat bot\n"
              , "appuyez sur 2 pour utiliser les fonctions prédéfinies")
        chatbot_ou_predefini = int(input())

    if chatbot_ou_predefini == 1:
        question = input("posez votre question : \n")
        liste_mot_question = fct_liste_mot_question(question)
        mot_question_present = fct_mot_question_present_dans_IDF(IDFdict, liste_mot_question)

        TFIDF_question = fct_TFIDF_question(mot_question_present, IDFdict)
        debut_reponse = fct_debut_reponse(question, TFIDF_question)

        similarite_president = similarite_vect(TFIDF_question, TFIDF, president_avec_numero, files_names)

        mot_question_plus_important = fct_mot_question_plus_important(TFIDF_question)

        reponse = fct_reponse(mot_question_plus_important, similarite_president, debut_reponse)
        print(reponse)

    if chatbot_ou_predefini == 2:
        print("Veuillez choisir la fonction que vous voulez utiliser :\n"
              , "1 :Affiche la liste des mots ayant le TF-IDF le plus bas dans l'ensemble des documents\n"
              , "2 :Affiche la liste des mots ayant le TF-IDF le plus élevé dans l'ensemble des documents\n"
              , "3 :Affiche les mots les plus répétés par le président Chirac\n"
              , "4 :Affiche les noms du des présidents qui a ont parlé de la « Nation » et celui qui l’a répété le plus de fois\n"
              , "5 :Affiche les présidents qui ont parler du climat et/ou de l’écologie\n"
              , "6 :Affiche les mots que les presidents ont évoquer, exeptés ceux dit par tous\n")
        fonctionchoisie = int(input())
        while fonctionchoisie < 1 or fonctionchoisie > 7:
            print("cette fonction n'existe pas, choisis en une autre")
            fonctionchoisie = int(input())

        if fonctionchoisie == 1:
            dis_par_tous = motsDisParTous(IDFdict)
            print(dis_par_tous)

        if fonctionchoisie == 2:
            TFIDFmoyen = moyenne(TFIDF)
            TFIDFmoyendecroissant = plusimportant(TFIDFmoyen)
            print(TFIDFmoyendecroissant)

        if fonctionchoisie == 3:
            TF2 = TF(occurence_president_2, files_names, president_avec_numero)
            dis_par_tous = motsDisParTous(IDFdict)
            Chiracmot = chiracSaidIt(TF2, dis_par_tous)
            print(Chiracmot)

        if fonctionchoisie == 4:
            presence_nation = mot_nation(TFIDF)
            print(presence_nation)

        if fonctionchoisie == 5:
            listecologie = ecologie(TFIDF)
            print(listecologie)

        if fonctionchoisie == 6:
            motevoque = mot_evoque_pas_par_tous(IDFdict)
            print(motevoque)
