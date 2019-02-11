# Projet générateur de site statique

## Installation avec pip

Le package étant disponible sur la plateforme pypi.org il est donc possible d'installer ce script avec pip :

    pip install Markdown2Html-French

Lien vers le package : https://pypi.org/project/Markdown2Html-French/

## Présentation du projet.

La finalité de ce projet était de développer un outil permettant la conversion de fichiers markdown en fichiers HTML.

## La liste des commandes.

Voici les commandes disponibles :

`-i` ou `--input-directory` accompagné du chemin vers le dossier où se trouvent les fichiers .md à convertir.

`-h` ou `--help`  affiche les aide pour les commandes.

## Comment ça marche ?

Ce script est simple d'utilisation.

Dans un terminal/CMD ou la console python et rendez vous dans le dossier ou ce trouve `sitestatique.py`.

Voici la commande a écrire :

    sitestatique.py -i Chemin_du_dossier_input -o Chemin_du_dossier_output
Ou

    sitestatique.py -input-directory Chemin_du_dossier_input -output-directory Chemin_du_dossier_output
Et pour avoir des beau arc-en-ciel il suffit de rajouter `-r` a la fin.

Comme ceci : 

    sitestatique.py -i Chemin_du_dossier_input -o Chemin_du_dossier_output -r
