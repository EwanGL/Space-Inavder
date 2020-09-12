import pygame # importation de la librairie pygame
import space
import os
import sys # pour fermer correctement l'application
current_path = os.path.dirname(__file__)
# lancement des modules inclus dans pygame
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont(None, 30)

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders") 
# chargement de l'image de fond
fond = pygame.image.load(os.path.join(current_path, 'background.png'))

# creation du joueur
player = space.Joueur()

# creation de l'ecran d'acceuil
start_menu = space.StartMenu()

# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)
listetir = []
listetir.append(space.Balle(player))
### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    if start_menu.running_game == True:
        screen.blit(fond,(0,0))

        player.sens = 0
        ### Gestion des événements  ###
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
                running = False # running est sur False
                sys.exit() # pour fermer correctement
        
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                tir.etat = "tiree"

        # Gestion du clavier      
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player.sens -= 1
            
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            player.sens += 1
            

        ### Actualisation de la scene ###

        # Points de vies
        listlives = []
        for life in range(player.lives):
            listlives.append(space.Heart())

        # Gestions des collisions
        for tir in listetir:
            for ennemi in listeEnnemis:
                if tir.toucher(ennemi) and tir.etat == 'tiree':
                    if ennemi.type == 2:
                        if len(listlives) < 3:
                            listlives.append(space.Heart())
                            player.lives +=1
                    listeEnnemis.remove(ennemi)
                    player.marquer(tir.etat)
                    tir.__init__(player)
                    listeEnnemis.append(space.Ennemi(player.score))
        
        #Gestion des munitions
        if listetir[(len(listetir)-1)].etat == 'tiree':
            listetir.append(space.Balle(player))
        
        for tir in listetir:
            if tir.rect.y <= 5:
                del tir

        # placement des objets

        # le joueur
        player.deplacer()
        screen.blit(player.image, player.rect) # appel de la fonction qui dessine le vaisseau du joueur
        
        # la balle
        for tir in listetir:
            tir.bouger(player)
            screen.blit(tir.image, tir.rect) # appel de la fonction qui dessine le vaisseau du joueur
        
        # les ennemis
        for ennemi in listeEnnemis:
            if ennemi.avancer() == False:
                listeEnnemis.remove(ennemi)
                listeEnnemis.append(space.Ennemi())
                if ennemi.type != 2:
                    if player.loose():
                        start_menu.running_game = False
            screen.blit(ennemi.image, ennemi.rect) # appel de la fonction qui dessine le vaisseau du joueur

        # les points de vies
        for i, life in enumerate(listlives):
            life.rect.x = i*30
            screen.blit(life.image, life.rect)
        # le score
        player.refresh_score()
        screen.blit(player.score_text, (700,0))
        pygame.display.update() # pour ajouter tout changement à l'écran

    else:
        screen.blit(start_menu.image,(0,0))
        screen.blit(start_menu.banner,(100,75))
        screen.blit(start_menu.button,start_menu.rect)
        for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
            if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre    
                running = False
                sys.exit
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_menu.rect.collidepoint(event.pos):
                    start_menu.running_game = True
                    player.__init__()
        pygame.display.update() # pour ajouter tout changement à l'écran