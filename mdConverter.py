import os

convertion = False
entre = ""

print("Pour afficher les commandes possibles tapez  '-h'")

def Convertirsimple(entre) :

    if (os.path.isfile(entre)) :

        with open(entre, "r") as file :

            lignes_file = file.read().splitlines()

            html_file = open(file.name[:-3]+".html", "a")

            unordered_list_open = False

            for i in range(len(lignes_file)) :

                ligne = lignes_file[i]

                if (ligne.startswith("# ")) :



                    html_file.write("<h1>" +ligne[2:]+ "</h1>")

                if (ligne.startswith("## ")):



                    html_file.write("<h2>" + ligne[3:] + "</h2>")

                if (ligne.startswith("### ")):



                    html_file.write("<h2>" + ligne[4:] + "</h2>")

                if (ligne.startswith("- ")):

                    if (unordered_list_open == False):

                        html_file.write("<ul>")
                        html_file.write("<li>" +ligne[2:] + "</li>")
                        unordered_list_open = True
                    else :
                        html_file.write("<li>" + ligne[2:] + "</li>")

                if not ligne.startswith("- ") and unordered_list_open:

                    unordered_list_open = False
                    html_file.write("</ul>")

                if (ligne.startswith("**")):

                    html_file.write("<strong>" + ligne[2:-2] + "</strong>")

                if (ligne.startswith("https://")):

                    html_file.write("<a href=\"" +ligne+ "\">"+ ligne +"</a>")

                if (ligne == ""):

                    html_file.write("<br>")




    else:

        print("le fichier n'existe pas")

while convertion == False :

    entre = input("-> ")
    entre = entre.split(" ")

    if (entre[0] == "-h" or entre[0] == "--help") :

        print("Voici les différentes commandes possibles :")
        print("")
        print("-h ou --help : affiche les différentes commandes possibles")
        print("-i ou --input-directory : indique le chemin du md a convertir")
        print("-o ou --output-directory : indique le chemin vers le dossier ou le fichier html sera déposé")

    elif ((entre[0] == "-i" or entre[0] == "--input-directory") and len(entre) == 2):

        Convertirsimple(entre[1])

    else:

        print("erreur dans la commande")