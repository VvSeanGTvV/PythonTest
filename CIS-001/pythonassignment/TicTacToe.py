##########################
#                        #
#      Tic Tac Toe       #
# VSTUDIOS & VvSeanGtvV  #
#     09 / 30 / 2026     #
#                        #
##########################

class Board:
    BoardCapacity: int = 0
    BoardSize: int = 0
    BoardData = [[]]
    def __init__(self, size:int):
        """
        Creates a board grid list
        """
        self.BoardCapacity = size*size
        self.BoardSize = size
        for y in range(size):
            self.BoardData.append([])
            for x in range(size):
                self.BoardData[y].append(" ")
    
    def placePlayer(self, player:chr, x:int, y:int):
        """
        Places the player on the given position, though first checked if the slot is empty
        Returns whether it was valid, otherwise false if it invalid
        """

        if (x > self.BoardSize or y > self.BoardSize or y < 0 or x < 0):
            print("Invalid Position")
            return False
        elif (self.isEmptySlot(x, y)): 
            self.BoardData[y][x] = player
            self.BoardCapacity -= 1
            return True
        else: 
            print(f"Spot x:{x} y:{y} is taken already!")
            return False

    def isEmptySlot(self, x:int, y:int):
        """
        Returns if the position given is a ' ' or just empty
        """
        return self.BoardData[y][x] == " "
    
    def WinnerByRow(self, player:chr):
        """
        Returns whether all rows have matching player
        """
        playerToCheck: chr = player
        xCount:int = 0
        for y in range(len(self.BoardData)-1):
            for i in range(len(self.BoardData[y])):
                if (playerToCheck == self.BoardData[y][i]): xCount += 1
                else: xCount = 0
            if (xCount >= self.BoardSize): return True
        return False

    def WinnerByCol(self, player:chr):
        """
        Returns whether all columns have matching player
        """
        playerToCheck: str = player
        yCount:int = 0
        for y in range(len(self.BoardData)-1):
            if (playerToCheck == self.BoardData[y][0]): yCount += 1
            else: yCount = 0
        return (yCount >= self.BoardSize)

    def WinnerByDiagonal(self, player:chr):
        """
        Returns whether all diagonals have matching player
        """
        playerToCheck: str = player
        dCount:int = 0
        for y in range(len(self.BoardData)-1):
            if (playerToCheck == self.BoardData[y][y]): dCount += 1
            else: dCount = 0
        if (dCount >= self.BoardSize): return True
        dCount:int = 0
        for y in range(len(self.BoardData)-1):
            if (playerToCheck == self.BoardData[y][(self.BoardSize-1)-y]): dCount += 1
            else: dCount = 0
        return (dCount >= self.BoardSize)
    
class RobotBoard:
    PredictionX: int = 0
    PredictionY: int = 0
    def __init__(self):
        pass

    def CalculateMove(self, board:Board):
        pass

def RenderBoard(board:Board):
    for y in range(len(board.BoardData)):
        BoardRenderY: str = ""
        for x in range(len(board.BoardData[y])):
            BoardRenderY = BoardRenderY + f"[{board.BoardData[y][x]}]"
        print(BoardRenderY)

Robot = RobotBoard()
BoardGame = Board(3) # Create a class of 3x3 grid list

PlayerTurn = 0
def play_game(botGame:bool=False):
    print("")
    global PlayerTurn # This is usually we make a variable global so that every outside function can reach the unreachable variable

    RenderBoard(BoardGame) # Renders the board

    # PLAYER's Variable
    row: int = 0
    col: int = 0
    PlayerList = ['X', 'O']
    Player: chr = PlayerList[PlayerTurn]
    
    print(f"Player {Player}'s Turn")

    # TRY & EXCEPT FUNCTION
    DoNotChangeTurn: bool = False # We need to not change turn when user fails to input the numbers
    try: # basically try and catch, useful to actually not crash when inputed wrong
        row = int(input("Row (0, 1, or 2): "))
        col = int(input("Column (0, 1, or 2): "))
    except Exception as e:
        DoNotChangeTurn = True
        print(f"No Value/{e}")

    hasWinner: bool = False
    if (not DoNotChangeTurn): 
        DoNotChangeTurn = not BoardGame.placePlayer(Player, row, col)
        if (not DoNotChangeTurn): 
            PlayerTurn += 1

    # WINNER FUNCTIONALITY
    hasWinner = BoardGame.WinnerByRow(Player) or BoardGame.WinnerByCol(Player) or BoardGame.WinnerByDiagonal(Player)
    if (PlayerTurn > len(PlayerList)-1): PlayerTurn = 0
    if (not hasWinner and BoardGame.BoardCapacity > 0): play_game() 
    elif (BoardGame.BoardCapacity <= 0): print("Tie!")
    else: print(f"Player {Player} is the Winner!")
    pass

if (__name__ == "__main__"):
    play_game()
    pass
