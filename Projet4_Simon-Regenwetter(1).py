from tkinter import*
from math import*

#Création de la fênetre principal 
fenetre = Tk()
fenetre.config(height=500, width=500)
fenetre.title("Triangle de Sierpinski")

#Création du Canevas
Canevas=Canvas(fenetre, height=500, width=500)
Canevas.place(x=0,y=0)

#Configuration de la fenêtre
fenetreConfig = Toplevel()
fenetreConfig.title("Configuration du Triangle")
fenetreConfig.config(width=400,height=250)
#Fenêtre en mode pop-up
fenetreConfig.grab_set()
fenetreConfig.transient(fenetreConfig.master)

#Création de la fonction de lancement du programme
def lancer():
    """ Cette fonction permet de lancer la création du triangle en demandant de cliquez 3 fois """
    iteration = int(entreeNombreIteration.get())
    fenetreConfig.destroy()
    liste = []
    clic = 0

    #Fonction permettant de recupérer le clic gauche de l'utilisateur
    def clicG(event):
        nonlocal clic
        liste.append(event.x)
        liste.append(event.y)
        clic += 1
        
        if clic == 3:
            #Fonction du dessin et calcul du triangle
            def Sierpinski(n, xA, yA, xB, yB, xC, yC):
                """ Cette fonction vous permet de créer un Triangle de sierpinski avec n comme variable d'itération, xA et yA
                comme coordonnées du sommet du triangle, xB, yB et xC, yC comme coordonnées des points restants """
                N = n
                A=[xA,yA]
                B=[xB,yB]
                C=[xC,yC]
                if N == 0:
                    triangle = Canevas.create_polygon(A[0], A[1], B[0], B[1], C[0], C[1], fill='red')

                else :
                    Sierpinski(n-1, (A[0]+B[0])/2 , (A[1]+B[1])/2, B[0], B[1], (C[0]+B[0])/2 , (C[1]+B[1])/2)
                    Sierpinski(n-1, (A[0]+C[0])/2 , (A[1]+C[1])/2, (C[0]+B[0])/2 , (C[1]+B[1])/2, C[0], C[1])
                    Sierpinski(n-1, A[0], A[1], (A[0]+B[0])/2 , (A[1]+B[1])/2, (A[0]+C[0])/2 , (A[1]+C[1])/2)

            Sierpinski(iteration, liste[0], liste[1], liste[2], liste[3], liste[4], liste[5])
    fenetre.bind('<Button-1>', clicG)
    
    


#Bouton de création du triangle
bouton = Button(fenetreConfig, text='Déssinez le Triangle', command=lancer)
bouton.config(height=2, bg='orange')
bouton.place(x=155, y=150)

#Texte explicatif du programme
textePresentation = Label(fenetreConfig, text="Créez votre triangle de Sierpinski ici,"+ '\n' +
"rentrez votre nombre d'itération ci-dessous puis "+'\n'+"cliquez sur le bouton."+'\n'+
"Puis cliquez 3 fois pour créer les 3 points du "+'\n'+
"triangle. Surprise votre triangle est créé !")
textePresentation.config(font= ('verdana' ,12 ,'normal' ),justify='left')
textePresentation.place(x=0, y=0)

#Texte de l'entrée d'itération
texteNombreIterationsateur = Label(fenetreConfig, text="Combien d'itération :")
texteNombreIterationsateur.config(font= ('verdana' ,12 ,'normal' ))
texteNombreIterationsateur.place(x=0,y=100)

#Entrée du nombre d'itération
entreeNombreIteration = Entry(fenetreConfig)
entreeNombreIteration.place(x=200, y=101)
entreeNombreIteration.config(width=8)
entreeNombreIteration.insert(0,'0')

fenetre.mainloop()