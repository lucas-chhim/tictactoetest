# 23/10

#  tic tac toe , version 0.1, lucas & fred

import os
 
os.system('cls') # cls= clear screen , upon linux operating system, its another command named : clear

""""
the point there being to clean up the terminal everytime we are gonna run the game

"""


# with the following commands we are creating the game board , dimension are cases of 3x3 so 9

def afficher_plateau(plateau_de_jeu):
    for ligne in plateau_de_jeu:
        print(" | ".join(ligne))
        print("-" * 9)
       
""""

here , we gonna define the game board , it's made of | and columns and rows
to do so we are using '-' , 9 x "-" , because we need 3 cases x 3 caracteres per lines


"""


def verifier_victoire(plateau_de_jeu, joueur):
    for ligne in plateau_de_jeu:
        if all(s == joueur for s in ligne):
            return True
    for col in range(3):
        if all(plateau_de_jeu[row][col] == joueur for row in range(3)):
            return True
    if all(plateau_de_jeu[i][i] == joueur for i in range(3)) or all(plateau_de_jeu[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def partie_tic_tac_toe():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueurs = ["X", "O"]
    tour = 0

    """
    with this def we are setting up players move X & O , its what gonna be on screen
   
    """



    while tour < 9:
        joueur = joueurs[tour % 2]
        afficher_plateau(plateau)
       
        while True:
            try:
                ligne = int(input(f"Player {joueur}, enter the line number (0, 1, 2) : "))
                col = int(input(f"Player {joueur}, enter the row number (0, 1, 2) : "))
                if plateau[ligne][col] == " ":
                    plateau[ligne][col] = joueur
                    break
                else:
                    print("This case is already taken, please try again")
            except (ValueError, IndexError):
                print("Entry is not valid, please choose between 0,1,2")

        if verifier_victoire(plateau, joueur):
            afficher_plateau(plateau)
            print(f"CONGRATULATIONS ! Player {joueur} win!")
            return

        tour += 1

    afficher_plateau(plateau)
    print("No One wins, Its a draw !")

if __name__ == "__main__":
    partie_tic_tac_toe()