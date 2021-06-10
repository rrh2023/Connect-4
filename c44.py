

import random  
from c43 import *

class AIPlayer(Player):
    """contructs an oject: AIPlayer, which is 
       a subclass of the object: Player
    """
    def __init__(self, checker, tiebreak, lookahead):
        """constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """returns a string representing the object: AIPlayer
        """
        if self.checker == "X":
            return 'Player X (' + self.tiebreak + ", " + str(self.lookahead) + ")"
        else:
            return 'Player O (' + self.tiebreak + ", " + str(self.lookahead) + ")"      
        
    def max_score_column(self, scores):
       """returns the column of the max score based on
          the AIPlayer's tiebreak strategy
       """
       max_score = max(scores)
       count = 0
       list_max_scores = []
       for i in range(len(scores)):
           if scores[i] == max_score:
               list_max_scores += [i]
               count += 1
       if count > 1:
           if self.tiebreak == "RANDOM":
               return random.choice(list_max_scores)
           elif self.tiebreak == "LEFT":
               return list_max_scores[0]
           elif self.tiebreak == "RIGHT":
               return list_max_scores[-1]
       else:
          return list_max_scores[0]
      
    def scores_for(self, b):
        """takes a Board object b and determiness the called AIPlayer's
           scores for the columns in b.
        """
        scores = [0] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.opponent_checker()) == True or b.is_win_for(self.checker) == True:
                     if b.is_win_for(self.checker) == True:
                         scores[col] = 100
                     else: 
                         scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                test_opp = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead - 1))
                opp_scores = test_opp.scores_for(b)
                if max(opp_scores) == 50:
                    scores[col] = 50
                elif max(opp_scores) == 0:
                     scores[col] = 100
                elif max(opp_scores) == 100:
                     scores[col] = 0
                else:
                    scores[col] = -1
                b.remove_checker(col)
        return scores
       
                
    def next_move(self, b):
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
        
               
               
            
               
           
           
            
   
        
