from c41 import Board


class Player(Board):
    def __init__(self, checker):
        """contructs an object: Player"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """returns a string representing the object: Player
        """
        if self.checker == "X":
            return 'Player X'
        else:
            return 'Player 0'
        
    def opponent_checker(self):
        """returns the opponent's checker"""
        if self.checker == 'X':
            return "O"
        else:
            return "X"
    
    def next_move(self, b):
        """accepts a Board object b as a parameter
           and returns the column where the player
           wants to make the next move.
        """
        col = int(input("Enter a column: \n"))
        while col not in [0,9,8,7,6,5,4,3,2,1]:
           col = int(input("Pick a column number!: \n"))
           if col in [0,1,2,3,4,5,6,7,8,9]:
               break
        while col not in range(b.width):
           col = int(input("Try again!: \n"))
           if col in range(b.width):
                    break
        if b.can_add_to(col) == True:
            self.num_moves += 1
            return col
       
        
         
        
           