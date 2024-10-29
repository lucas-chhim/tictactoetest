# 29/10

#  tic tac toe , version 0.1b, lucas & fred

import os
 
os.system('cls') # cls= clear screen , upon linux operating system, its another command named : clear

""""
the point there being to clean up the terminal everytime we are gonna run the game

"""


# with the following commands we are creating the game board , dimension are cases of 3x3 so 9 

def afficher_plateau(plateau_de_jeu):
    for ligne in plateau_de_jeu:
        print( " | ".join(ligne))
        print("-" * 9) 
        
""""

here , we gonna define the game board , its made of | and columns and rows
to do so we are using '-' , 9 x "-" , because its 3 cases x 3 carachters per lines 


"""


def VERIFIER_VICTOIRE(plateau_de_jeu, joueur):
    for ligne in plateau_de_jeu:
        if all(s == joueur for s in ligne):
            return True
    for col in range(3):
        if all(plateau_de_jeu[row][col] == joueur for row in range(3)):
            return True
    if all(plateau_de_jeu[i][i] == joueur for i in range(3)) or all(plateau_de_jeu[i][2 - i] == joueur for i in range(3)):
        return True
    return False

# commands above are players victory checks




def PARTIE_TIC_TAC_TOE():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueurs = ["X", "O"]                                                    # here we define 2 plahyers and their moves
    tour = 0                                                            # we start the game here , 9 round maximum, this is an incrementation of + 1 per round

   



    while tour < 9:    # tour checks
        joueur = joueurs[tour % 2]
        afficher_plateau(plateau) # game board drawing
       
        while True:
            try:
                ligne = int(input(f"Player {joueur}, enter the line number (0, 1, 2) : ")) # player input line 
                col = int(input(f"Player {joueur}, enter the row number (0, 1, 2) : "))  # player input row, columns
                if plateau[ligne][col] == " ":
                    plateau[ligne][col] = joueur
                    break
                else:
                    print("This case is already taken, please try again")  # error message when a case is already took
            except (ValueError, IndexError):
                print("Entry is not valid, please choose between 0,1,2") # error message when a case numnber is not in the range 0 1 2

        if VERIFIER_VICTOIRE(plateau, joueur):
            afficher_plateau(plateau)
            print(f"CONGRATULATIONS ! Player {joueur} win!") # victory message
            return

        tour += 1                                                       # here we do add +1 to the round

    afficher_plateau(plateau)
    print("No One wins, Its a draw !") # this message is on display when its a draw 

if __name__ == "__main__": #main
    PARTIE_TIC_TAC_TOE()
