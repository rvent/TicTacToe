class Board(object):
    
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.gameboard = {}
        for i in range(rows):
            self.gameboard[i+1] = ["-"]*columns
    
    @property
    def formatted_board(self):
        """Used only to view the gameboard
           prints out a formatted gameboard and 
           returns the size of the board."""
        return self.format_board(self.gameboard) 
    
    @property
    def board(self):
        """a getter for the gameboard"""
        return self.gameboard
    
    @board.setter
    def board(self, change):
        self.gameboard[change[0]][change[1]] = change[2]

    def format_board(self, board, message=""):
        print(f"{message}")
        for i in board:
            print(board[i])
        return f'{len(board.keys())} x {len(board[1])} Board'
    
class Player(object):
    
    def __init__(self, name, board, side="x"):
        self.board = board
        self._name = name
        self.side = side
        
    def valid_move(self, row, column):
        if board.board[row][column] != "-":
            return False
        else:
            return True
        
    def make_move(self, row, column):
        if self.valid_move(row, column):
            board.board(row, column, self.side)
        else:
            return "Invalid Move"
            
    
class TicTacToe(Board):
    
    def __init__(self, rows=3, columns=3):
        Board.__init__(self, rows, columns)
        self._rows = rows
        self._columns = columns
