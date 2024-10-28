# 23/10

# Tic Tac Toe, version 0.1, Lucas & Fred

import os
 
os.system('cls') # cls = clear screen; on Linux systems, the equivalent command is 'clear'

"""
The purpose here is to clear the terminal each time we run the game.
"""

# The following commands create the game board, which is a 3x3 grid, so 9 cells in total.

def afficher_plateau(plateau_de_jeu):
    for ligne in plateau_de_jeu:
        print(" | ".join(ligne))
        print("-" * 9) 
        
"""
Here, we define the game board, made up of columns and rows using '|'.
To separate rows, we use '-' repeated 9 times, as each row has 3 cells with 3 characters per line.
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

# The commands above check for a player's victory.

def PARTIE_TIC_TAC_TOE():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueurs = ["X", "O"]  # Define two players and their symbols
    tour = 0  # Start the game, with a maximum of 9 rounds; this is incremented by +1 each round

    while tour < 9:  # Round check
        joueur = joueurs[tour % 2]
        afficher_plateau(plateau)  # Draw the game board
       
        while True:
            try:
                ligne = int(input(f"Player {joueur}, enter the line number (0, 1, 2): "))  # Player inputs line
                col = int(input(f"Player {joueur}, enter the column number (0, 1, 2): "))  # Player inputs column
                if plateau[ligne][col] == " ":
                    plateau[ligne][col] = joueur
                    break
                else:
                    print("This cell is already taken, please try again")  # Error message if cell is taken
            except (ValueError, IndexError):
                print("Invalid entry, please choose between 0, 1, and 2")  # Error if input is out of range

        if VERIFIER_VICTOIRE(plateau, joueur):
            afficher_plateau(plateau)
            print(f"CONGRATULATIONS! Player {joueur} wins!")  # Victory message
            return

        tour += 1  # Increment round

    afficher_plateau(plateau)
    print("It's a draw!")  # Message displayed in case of a draw

if __name__ == "__main__":  # Main
    PARTIE_TIC_TAC_TOE()
