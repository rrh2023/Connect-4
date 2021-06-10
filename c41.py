
class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.slots = [[" "] * self.width for row in range(self.height)]
    
    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s += '-'
        for hyphen in range(self.width):
            s += '--'
        s += '\n'
        
        x = 0
        s += ' '
        for number in range (self.width):
            s += str(x) + ' '
            if x != 9:
                x +=1
            elif x == 9:
                x = 0
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        for row in range(self.height):
            if row == self.height - 1:
                if self.slots[row][col] == " ":
                    self.slots[row][col] = checker
            elif row in range(self.height - 1):
                if self.slots[row][col] == " " and self.slots[row + 1][col] != " ":
                    self.slots[row][col] = checker
        
    ### add your reset method here ###
    def reset(self):
        """resets the board to an empty board without checkers"""
        for j in range(self.height):
            for i in range(self.width):
                self.slots[j][i] = " "    
                
        
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        if col not in range(self.width):
            return False
        for row in range(self.height):
            if self.slots[row][col] == " ":
                return True 
        return False
    
    
    def is_full(self):
        for row in range(self.height):
            for col in range (self.width):
                if self.slots[row][col] == " ":
                    return False
        return True
            
        
    def remove_checker(self, col):
        for row in range(self.height):
            if self.slots[row][col] != " ":
                self.slots[row][col] = " "
                break
            
    #def is_win_for(self, checker):
        
    def is_vertical_win(self, checker):
        """checks for a vertical win in the Board object"""
        for row in range(self.height - 3):
           for col in range(self.width):
               if self.slots[row][col] == checker and \
                  self.slots[row + 1][col] == checker and \
                  self.slots[row + 2][col] == checker and \
                  self.slots[row + 3][col] == checker:
                      return True
        return False
               
    def is_horizontal_win(self, checker):
        """checks for a horizontal win in the Board object"""
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                       return True
        return False
        
    def is_down_lr_win(self, checker):
        """checks for a downward, left-to-right win"""
        for row in range(self.height - 3):
           for col in range(self.width - 3):
               if self.slots[row][col] == checker and \
                  self.slots[row + 1][col + 1] == checker and \
                  self.slots[row + 2][col + 2] == checker and \
                  self.slots[row + 3][col + 3] == checker:
                      return True
        return False

    def is_up_lr_win(self, checker):
        """checks for an upward, left-to-right win"""
        for row in range(self.height - 3):
           for col in range(3, self.width):
               if self.slots[row][col] == checker and \
                  self.slots[row + 1][col - 1] == checker and \
                  self.slots[row + 2][col - 2] == checker and \
                  self.slots[row + 3][col - 3] == checker:
                      return True
        return False
    
    def is_win_for(self, checker):
        if self.is_vertical_win(checker) == True or \
           self.is_horizontal_win(checker) == True or \
           self.is_down_lr_win(checker) == True or \
           self.is_up_lr_win(checker) == True:
               return True
        else: 
            return False
                
  
        
           