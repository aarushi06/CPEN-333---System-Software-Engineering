# student name: Aarushi Mehra
# student number: 82519695
import random

class TicTacToe:
    def __init__(self): # Use as is
        """ initializes data fields (board and played) 
            and prints the banner messages 
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell, 
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells 
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()

    def printBoard(self) -> None:        
        """ prints the board on the screen based on the values in the self.board data field """

        print('\n')
        print('\t', self.board[0] , ' | ', self.board[1] , ' | ', self.board[2], '\t', '0', ' | ', '1', ' | ', '2')
        print('\t', '--', '+' , '---', '+', '--', '\t','--', '+' , '---', '+', '--' )
        print('\t', self.board[3] , ' | ', self.board[4] , ' | ', self.board[5], '\t', '3', ' | ', '4', ' | ', '5')
        print('\t', '--', '+' , '---', '+', '--', '\t','--', '+' , '---', '+', '--' )
        print('\t', self.board[6] , ' | ', self.board[7] , ' | ', self.board[8], '\t', '6', ' | ', '7', ' | ', '8', '\n')
    

    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number; 
            error checks that the input is a valid cell number; 
            and prints the info and the updated self.board;
        """
        input_type = False  #flag to check for the while loop
        while (not input_type):
            try:
                input_cell = int(input('Next move for X (state a valid cell num): '))
                if input_cell in self.played or input_cell > 8 or input_cell < 0:
                    print('Must enter a valid cell number')
                elif type(input_cell) == int:
                    self.played.update([input_cell])
                    self.board[input_cell]='X'
                    print('You chose cell ', input_cell)
                    input_type = True    #input is valid so get out of the loop
                    
            except ValueError:
                print('Must be an integer')

        self.printBoard()

    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell, 
            and prints the info and the updated self.board 
        """

        computer_played_valid = True
        while computer_played_valid and self.board.count('X') < 5:   #check if count of X is < 5 for valid no of moves
            computer_plays = random.randint(0,8)            
            if computer_plays not in self.played:
                self.played.update([computer_plays])
                self.board[computer_plays]='O'
                print('Computer chose cell ', computer_plays)
                computer_played_valid = False    #to get our of the while loop
            
        self.printBoard()


    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """

        winning_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        
        for row in range(len(winning_combinations)):
            win = []
            for col in range(len(winning_combinations[row])):
               
                if self.board[winning_combinations[row][col]] == who:  #to check individual cell in the sequence
                    win.append('True')
                else:
                    win.append('False')
                    
            if win.count('True') == 3:
                who_won = True     #to check if the sequence wins
                break
            
            else:
                who_won = False
                
        return who_won
                                            
    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or 
                 "You lost! Thanks for playing." or 
                 "A draw! Thanks for playing."  
        """
        counter_X = self.board.count('X')
        counter_O = self.board.count('O')
        
        if counter_X + counter_O < 9:
            win_update = self.hasWon(who)
            
            if win_update == True and who == 'X':
                print("You won! Thanks for playing.")
                return True
            if win_update == True and who == 'O':
                print("You lost! Thanks for playing.")
                return True
            
            else: return False

        else:
            print("A draw! Thanks for playing.")
            return True


if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate
