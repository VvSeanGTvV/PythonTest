##########################
#                        #
#      Tic Tac Toe       #
# VSTUDIOS & VvSeanGtvV  #
#     09 / 30 / 2026     #
#                        #
##########################

# Changelog:
# 10 / 04 / 2026 - AI MinMax Test
# 10 / 05 / 2026 - AI MinMax Finalized + ton of bugfix

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
        for x in range(self.BoardSize):
            for y in range(len(self.BoardData)-1):
                
                if (playerToCheck == self.BoardData[y][x]): yCount += 1
                else: yCount = 0
            if (yCount >= self.BoardSize): return True
        return False

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
    PlayerChr: chr = ''
    BotChr: chr = ''
    def __init__(self):
        pass

    def CalculateMove(self, board:Board):
        bestScore: float = float("-inf")
        bestMove = None

        for y in range(board.BoardSize):
            for x in range(board.BoardSize):
                if board.isEmptySlot(x, y):
                    board.BoardData[y][x] = self.BotChr
                    board.BoardCapacity -= 1

                    score: float = self.MinMax(board, False)
                    #print("TESTING: ", x, y, score)

                    board.BoardData[y][x] = " "
                    board.BoardCapacity += 1
                    
                    if score is not None and score > bestScore:
                        bestScore = score
                        bestMove = (x, y)

        if bestMove is not None:
            self.PredictionX = bestMove[0]
            self.PredictionY = bestMove[1]

            #print(f"AI chooses move at {bestMove} with score {bestScore}")
            return bestMove[0], bestMove[1]
    
    def SetPlayer(self, player:chr):
        self.PlayerChr = player

    def SetBot(self, player:chr):
        self.BotChr = player
    
    def MinMax(self, board: Board, maximizing: bool):
        if BoardGame.WinnerByRow(self.BotChr) or BoardGame.WinnerByCol(self.BotChr) or BoardGame.WinnerByDiagonal(self.BotChr): return 1
        if BoardGame.WinnerByRow(self.PlayerChr) or BoardGame.WinnerByCol(self.PlayerChr) or BoardGame.WinnerByDiagonal(self.PlayerChr): return -1
        if board.BoardCapacity == 0: return 0

        if maximizing:
            bestScore: float = float("-inf")

            for y in range(board.BoardSize):
                for x in range(board.BoardSize):
                    if board.isEmptySlot(x, y):
                        board.BoardData[y][x] = self.BotChr
                        board.BoardCapacity -= 1

                        score: float = self.MinMax(board, False)

                        board.BoardData[y][x] = " "
                        board.BoardCapacity += 1

                        bestScore: float = max(bestScore, score)
            return bestScore
        else:
            bestScore: float = float("inf")

            for y in range(board.BoardSize):
                for x in range(board.BoardSize):
                    if board.isEmptySlot(x, y):
                        board.BoardData[y][x] = self.BotChr
                        board.BoardCapacity -= 1

                        score: float = self.MinMax(board, True)

                        board.BoardData[y][x] = " "
                        board.BoardCapacity += 1

                        bestScore: float = min(bestScore, score)
            return bestScore

def RenderBoard(board:Board):
    for y in range(len(board.BoardData)-1):
        print("+---"*(len(board.BoardData)-1) + "+")
        BoardRenderY: str = ""
        for x in range(len(board.BoardData[y])):
            BoardRenderY = BoardRenderY + f"| {board.BoardData[y][x]} "
        print(f"{BoardRenderY}|")
    print("+---"*(len(board.BoardData)-1) + "+")

# --- FUNCTION ---

BotGameMode = False
PlayerTurn = 0

try: # basically try and catch, useful to actually not crash when inputed wrong
    b = input(f"Bot? [Y] [N]\n")
    if (b.lower() == "y" or b.lower() == "yes" or b.lower() == "ye" or b.lower() == "true" or b == 1): BotGameMode = True
    if (b.lower() == "n" or b.lower() == "no" or b.lower() == "false" or b == 0): BotGameMode = False
except (Exception, ValueError) as e:
    print(f"Invalid? {e}")

Robot = RobotBoard()
BoardGame = Board(3) # Create a class of 3x3 grid list

def play_game():
    print("")
    global PlayerTurn # This is usually we make a variable global so that every outside function can reach the unreachable variable
    global BotGameMode

    RenderBoard(BoardGame) # Renders the board

    # PLAYER's Variable
    player: int = 0
    row: int = 0
    col: int = 0
    PlayerList = ['X', 'O']
    Player: chr = PlayerList[PlayerTurn]
    DoNotChangeTurn: bool = False # We need to not change turn when user fails to input the numbers
    
    print(f"Player {Player}'s Turn")
    if BotGameMode and PlayerTurn != player:
        Robot.SetPlayer(PlayerList[player])
        Robot.SetBot(Player)
        try: # basically try and catch, useful to actually not crash when inputed wrong
            row, col = Robot.CalculateMove(BoardGame)
        except Exception as e:
            DoNotChangeTurn = True
            print(f"No Value/{e}")
    else:
        try: # basically try and catch, useful to actually not crash when inputed wrong
            row = int(input(f"Row (0 -> {BoardGame.BoardSize-1}): "))
            col = int(input(f"Column (0 -> {BoardGame.BoardSize-1}): "))
            if (row > BoardGame.BoardSize-1): raise ValueError
            if (col > BoardGame.BoardSize-1): raise ValueError
        except (Exception, ValueError) as e:
            DoNotChangeTurn = True
            print(f"Invalid Move! {e}")

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
