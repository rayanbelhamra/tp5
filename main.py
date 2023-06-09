from random import choice

import arcade

import game_state
# import arcade.gui

from attack_animation import AttackType, AttackAnimation
from game_state import GameState

SCREEN_WIDTH = 1024

SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):
    """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

    PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
    PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
    COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
    COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
    ATTACK_FRAME_WIDTH = 154 / 2
    ATTACK_FRAME_HEIGHT = 154 / 2

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.pc_choice = None
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        self.player = None
        self.computer = arcade.Sprite('assets/compy.png', 1.5)
        self.players = arcade.Sprite('assets/faceBeard.png', 0.3)
        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.player_score = 0
        self.computer_score = 0
        self.rock_computer = AttackAnimation(AttackType.ROCK)
        self.rock_computer.scale = 0.4
        self.rock_computer.center_x = 900
        self.rock_computer.center_y = 200
        self.paper_computer = AttackAnimation(AttackType.PAPER)
        self.paper_computer.scale = 0.35
        self.paper_computer.center_x = 900
        self.paper_computer.center_y = 200
        self.scissors_computer = AttackAnimation(AttackType.SCISSORS)
        self.scissors_computer.scale = 0.35
        self.scissors_computer.center_x = 900
        self.scissors_computer.center_y = 200
        self.player_attack_type = {}
        self.computer_attack_type = None
        self.player_attack_chosen = False
        self.player_won_round = False
        self.draw_round = False
        self.game_state = game_state.GameState.NOT_STARTED

    def setup(self):
        """
       Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
       fois si vous recommencer une nouvelle partie.
       """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # Prenez note que vous devriez attribuer une valeur à tous les attributs créés dans __init__

        pass

    def draw_menu(self):
        """
       Dessiner le menu du jeu
       """
        arcade.draw_text(SCREEN_TITLE,
                         0,
                         SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                         arcade.color.BLACK_BEAN,
                         60,
                         width=SCREEN_WIDTH,
                         align="center")

        self.draw_instructions()
        self.players.center_x = 100
        self.players.center_y = 300
        self.players.draw()
        self.computer.center_x = 900
        self.computer.center_y = 300
        self.computer.draw()
        self.rock.center_x = 25
        self.rock.center_y = 200
        self.paper.center_x = 100
        self.paper.center_y = 200
        self.scissors.center_x = 175
        self.scissors.center_y = 200
        arcade.draw_rectangle_outline(900, 200, 50, 50, arcade.color.BLACK_BEAN, 5)
        self.draw_scores()
        arcade.draw_text(f"le pointage du joueur est {self.player_score}", -312.5, 75, arcade.color.BABY_PINK, 20, width=SCREEN_WIDTH,
                         align="center")
        arcade.draw_text(f"le pointage de l'ordinateur est {self.computer_score}", 300, 75, arcade.color.BABY_PINK, 20,
                         width=SCREEN_WIDTH, align="center")

    def validate_victory(self):
        """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """
        if self.game_state == GameState.ROUND_ACTIVE and self.player_attack_chosen :
            self.pc_choice = choice([AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS])
            print(self.pc_choice, self.player_attack_type)
            if self.player_attack_type == self.pc_choice:
                self.draw_round = True
                self.player_won_round = False
            elif self.player_attack_type == AttackType.ROCK and self.pc_choice == AttackType.SCISSORS:
                self.player_won_round = True
                self.player_score += 1
            elif self.player_attack_type == AttackType.PAPER and self.pc_choice == AttackType.ROCK:
                self.player_won_round = True
                self.player_score += 1
            elif self.player_attack_type == AttackType.SCISSORS and self.pc_choice == AttackType.PAPER:
                self.player_won_round = True
                self.player_score += 1
            else:
                self.player_won_round = False
                self.computer_score += 1
            self.player_attack_chosen = False
            self.game_state = GameState.ROUND_DONE

    def draw_possible_attack(self):
        """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
        pass

    def draw_attack(self):
        """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
        arcade.draw_rectangle_outline(25, 200, 50, 50, arcade.color.BLACK_BEAN, 5)
        arcade.draw_rectangle_outline(100, 200, 50, 50, arcade.color.BLACK_BEAN, 5)
        arcade.draw_rectangle_outline(175, 200, 50, 50, arcade.color.BLACK_BEAN, 5)
        if self.player_attack_type == AttackType.ROCK:
            self.rock.draw()
        elif self.player_attack_type == AttackType.PAPER:
            self.paper.draw()
        elif self.player_attack_type == AttackType.SCISSORS:
            self.scissors.draw()
        if self.pc_choice == AttackType.ROCK:
            self.rock_computer.draw()
        elif self.pc_choice == AttackType.PAPER:
            self.paper_computer.draw()
        else:
            self.scissors_computer.draw()

    def draw_scores(self):
        """
       Montrer les scores du joueur et de l'ordinateur
       """
        pass

    def draw_instructions(self):
        """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text("Appuyer sur espace pour commencer",
                             0,
                             SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                             arcade.color.BLACK_BEAN,
                             30,
                             width=SCREEN_WIDTH,
                             align="center")
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text("Choisissez votre attaque",
                             0,
                             SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                             arcade.color.BLACK_BEAN,
                             30,
                             width=SCREEN_WIDTH,
                             align="center")
            arcade.draw_rectangle_outline(25, 200, 50, 50, arcade.color.BLACK_BEAN, 5)
            arcade.draw_rectangle_outline(100, 200, 50, 50, arcade.color.BLACK_BEAN, 5)
            arcade.draw_rectangle_outline(175, 200, 50, 50, arcade.color.BLACK_BEAN, 5)
            self.rock.draw()
            self.paper.draw()
            self.scissors.draw()
        elif self.game_state == GameState.ROUND_DONE:
            self.draw_attack()
            if self.draw_round and not self.player_won_round:
                arcade.draw_text("Égalité",
                                 0,
                                 SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                 arcade.color.BLACK_BEAN,
                                 30,
                                 width=SCREEN_WIDTH,
                                 align="center")
            elif self.player_won_round:
                arcade.draw_text("Vous avez gagné",
                                 0,
                                 SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                 arcade.color.BLACK_BEAN,
                                 30,
                                 width=SCREEN_WIDTH,
                                 align="center")
            else:
                arcade.draw_text("Vous avez perdu",
                                 0,
                                 SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                 arcade.color.BLACK_BEAN,
                                 30,
                                 width=SCREEN_WIDTH,
                                 align="center")
            arcade.draw_text("Appuyer sur espace pour continuer",
                             0,
                             SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 5,
                             arcade.color.BLACK_BEAN,
                             30,
                             width=SCREEN_WIDTH,
                             align="center")
            if self.player_score == 3:
                self.game_state = GameState.GAME_OVER
            elif self.computer_score == 3:
                self.game_state = GameState.GAME_OVER

        elif self.game_state == GameState.GAME_OVER:
            self.draw_attack()
            if self.player_score == 3:
                arcade.draw_text("Vous avez gagné la partie",
                                 0,
                                 SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                 arcade.color.BLACK_BEAN,
                                 30,
                                 width=SCREEN_WIDTH,
                                 align="center")
            elif self.computer_score == 3:
                arcade.draw_text("Vous avez perdu la partie",
                                 0,
                                 SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4,
                                 arcade.color.BLACK_BEAN,
                                 30,
                                 width=SCREEN_WIDTH,
                                 align="center")
            arcade.draw_text("Appuyer sur espace pour recommencer",
                             0,
                             SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 5,
                             arcade.color.BLACK_BEAN,
                             30,
                             width=SCREEN_WIDTH,
                             align="center")


    def on_draw(self):
        """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".
        arcade.start_render()

        # Display title
        self.draw_menu()
        self.draw_instructions()
        self.draw_possible_attack()
        self.draw_scores()

        # afficher l'attaque de l'ordinateur selon l'état de jeu
        # afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
        pass

    def on_update(self, delta_time):
        """
       Toute la logique pour déplacer les objets de votre jeu et de
       simuler sa logique vont ici. Normalement, c'est ici que
       vous allez invoquer la méthode "update()" sur vos listes de sprites.
       Paramètre:
           - delta_time : le nombre de milliseconde depuis le dernier update.
       """
        # vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
        # si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
        # changer l'état de jeu si nécessaire (GAME_OVER)

        self.validate_victory()
        self.rock_computer.on_update()
        self.paper_computer.on_update()
        self.scissors_computer.on_update()
        self.rock.on_update()
        self.paper.on_update()
        self.scissors.on_update()

    def on_key_press(self, key, key_modifiers):
        """
       Cette méthode est invoquée à chaque fois que l'usager tape une touche
       sur le clavier.
       Paramètres:
           - key: la touche enfoncée
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

       Pour connaître la liste des touches possibles:
       http://arcade.academy/arcade.key.html
       """
        if (self.game_state == game_state.GameState.NOT_STARTED and key == arcade.key.SPACE):
            self.game_state = game_state.GameState.ROUND_ACTIVE
        if (self.game_state == game_state.GameState.ROUND_DONE and key == arcade.key.SPACE):
            self.game_state = game_state.GameState.ROUND_ACTIVE
        if (self.game_state == game_state.GameState.GAME_OVER and key == arcade.key.SPACE):
            self.game_state = game_state.GameState.NOT_STARTED

    def reset_round(self):
        """
       Réinitialiser les variables qui ont été modifiées
       """
        if self.game_state == GameState.GAME_OVER:
            self.player_score = 0
            self.computer_score = 0
            self.player_attack_chosen = False

        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """

        # Test de collision pour le type d'attaque (self.player_attack_type).
        # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True

        if self.rock.collides_with_point((x, y)):
            self.player_attack_type = AttackType.ROCK
            self.player_attack_chosen = True

        if self.paper.collides_with_point((x, y)):
            self.player_attack_type = AttackType.PAPER
            self.player_attack_chosen = True

        if self.scissors.collides_with_point((x, y)):
            self.player_attack_type = AttackType.SCISSORS
            self.player_attack_chosen = True


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
