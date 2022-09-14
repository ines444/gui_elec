# gui_elec

Aide pour la création du git:

1/ (github.com) Se créer un compte sur github (https://github.com/). 


2/ (github.com) Télécharger et installer MingW64 (https://www.mingw-w64.org/downloads/) qui permet de gérer les dossiers git en local. 
3/ (Terminal Git Bash) Ouvrir le Git Bash dans le dossier en local où on veut que le dossier git se trouve (clique droit dans ce dossier et "Git Bash here") puis, grâce au terminal Git Bash, créer une clé SSH pour la communication entre le dossier local et github (tuto: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). 


4/ (github.com) Ajouter la clé SSH au compte github (tuto: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). 


5/ Demander à devenir collaborateur du 'repository' https://github.com/ines444/gui_elec.


6/ (Terminal Git Bash) Cloner le dossier github localement en utilisant la commande 'git clone git@github.com:username/project-name.git new-project-name' (tuto entier: https://gist.github.com/ericconrad/ccc1af3cd12a69ef2e6e)


7/ Ensuite pour ajouter des dossiers au git, le faire en local (simplement copier coller dans le dossier git). 


8/ Pour partager les modifications d'un fichier 'new_file' sur github: 
	- git add new_file
	- git commit -m "Message expliquant les modifications (exemple: Fonction X ajoutée)"
	- git push origin main

	
9/ Ensuite les modifications apportées sont visibles en ligne, et l'historique des commits permet de les retracer. 