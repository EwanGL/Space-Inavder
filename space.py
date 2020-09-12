import pygame  # necessaire pour charger les images et les sons
import os
import random
current_path = os.path.dirname(__file__)

pygame.font.init()
myfont = pygame.font.SysFont(None, 30)

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path, 'vaisseau.png'))
        self.sens = 0
        self.score = 0
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 475
        self.lives = 3

    def refresh_score(self):
        self.score_text = myfont.render(f'Score: {self.score}', False, (255, 255, 255))

    def loose(self):
        self.lives -= 1
        if self.lives == 0:
            print(f'Vous avez perdu , votre score est: {self.score}')
            return True
    
    def marquer(self, etat):
        if etat != 'chargee':
            self.score += 1
    
    def deplacer(self):
            if self.rect.x >= 5 and self.rect.x <=735:
                self.rect.x += self.sens*5
            elif self.rect.x >735:
                self.rect.x -= 5
            elif self.rect.x <5:
                self.rect.x +=5
class Balle(): #classe pour créer la balle
    def __init__(self, player):
        self.tireur = Joueur
        self.image = pygame.image.load(os.path.join(current_path, 'balle.png'))
        self.etat = 'chargee'
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = 475
    
    def toucher(self, ennemi):
        if pygame.sprite.collide_rect(self, ennemi) != 0:
            return True
        else:
            return False
    def bouger(self, player):
        if self.etat == 'chargee':
            self.rect.x = player.rect.x
        elif self.etat == 'tiree':
            self.rect.y -= 7

class Ennemi(): #classe pour créer les ennemies
    NbEnnemis = 5
    def __init__(self, kills=0, mission=6):
        if mission == 6:
            self.type = random.choice([0,1,2])
        else:
            self.type = random.choice([0,1])
        
        if self.type == 0:
            self.image = pygame.image.load(os.path.join(current_path, 'invader1.png'))
            if kills >20:
                self.vitesse = 2
            else:
                self.vitesse = 1
        
        elif self.type == 1:
            self.image = pygame.image.load(os.path.join(current_path, 'invader2.png'))
            if kills >20:
                self.vitesse = 2
            else:
                self.vitesse = 1
        
        elif self.type == 2:
            self.image = pygame.image.load(os.path.join(current_path, 'heart.png'))
            if kills >20:
                self.vitesse = 3
            else:
                self.vitesse = 2
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,732)
        self.rect.y = 64


    def avancer(self):
        if self.rect.y >= 475:
            return False
        else:
            self.rect.y += self.vitesse

class Heart(): #classe pour créer les coeurs(pts de vie)
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path, 'heart.png'))
        self.rect = self.image.get_rect()

class StartMenu():
    def __init__(self):
        self.image = pygame.image.load(os.path.join(current_path, 'background.png'))
        self.banner = pygame.image.load(os.path.join(current_path, 'banner.png'))
        self.button = pygame.image.load(os.path.join(current_path, 'play.png'))
        self.rect = self.button.get_rect()
        self.rect.x = 275
        self.rect.y = 300
        self.running_game = False