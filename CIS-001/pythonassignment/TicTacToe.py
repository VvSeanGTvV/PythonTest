import random, os

##########################
#                        #
#      Tic Tac Toe       #
# VSTUDIOS & VvSeanGtvV  #
#     09 / 30 / 2026     #
#                        #
##########################

# Changelog:
# 10 / 04 / 2026 - AI MinMax Test
# 10 / 05 / 2026 - AI MinMax Finalized + Bugfix
# 10 / 12 / 2026 - AI MinMax Fix, holy it is the unbeatable AI version + Clear Console + AI MinMax Multibot Support + Changed the ordering of the bot choice from begin and end to just beginning of the function
# 10 / 14 / 2026 - Updated its docstring for anyone wondering what it do + Bugfix

class Board:
    BoardCapacity: int = 0
    BoardSize: int = 0
    BoardData = [[]]
    def __init__(self, size:int):
        """
        Creates a board in a grid list or array
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

        Returns True when valid move, False when invalid move has made
        """

        if (x > self.BoardSize or y > self.BoardSize or y < 0 or x < 0):
            return False
        elif (self.isEmptySlot(x, y)): 
            self.BoardData[y][x] = player
            self.BoardCapacity -= 1
            return True
        else:  # if for some reason none of the if and elif is true, this would result False for fallback
            return False

    def isEmptySlot(self, x:int, y:int):
        """
        Returns if the position given is a ' ' or just empty
        """
        return self.BoardData[y][x] == " "
    
    def CleanBoard(self):
        """
        Clean up the board, basically empty out.
        """
        for y in range(self.BoardSize):
            for x in range(self.BoardSize):
                self.BoardData[y][x] = ' '
        self.BoardCapacity = self.BoardSize*self.BoardSize
    
    def WinnerByRow(self, player:chr):
        """
        0 -> BoardSize (X)

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
        0 -> BoardSize (Y)

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
        0 -> BoardSize (X & Y) including -X, +X, -Y, +Y

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

# The Robot Board is using an algorithm called Minimax
# It's one of the most common algorithm used for 
# Tic-Tac-Toe | Chess | Checkers | Connect Four
# Mainly meant for two players but this was modified
# to have go against multiple than just one person, dynamic to have many bots
class RobotBoard: # I call him MinMAXX
    Players = [] # Players or bots List which are up against
    BotChr: chr = '' # The bot itself playing currently
    def __init__(self):
        """
        Creates a Robot or Bot for the board
        """
        pass # no data needed

    def CalculateMove(self, board:Board):
        """
        Calculates its next best move, dependent on Mini Max Algorithm.
        It go against (extras AI, if any) and/or Player

        Returns (x, y)
        """
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
                    
                    if score is not None and score > bestScore: # It only uses the best move when the score is actually good than the best score
                        bestScore = score
                        bestMove = (x, y)

        if bestMove is not None: # Return the move back
            #print(f"AI chooses move at {bestMove} with score {bestScore}")
            return bestMove[0], bestMove[1]
    
    def SetPlayer(self, players):
        #print(players)
        self.Players = players

    def SetBot(self, player:chr):
        self.BotChr = player
    
    def MinMax(self, board: Board, maximizing: bool):
        """
        Maxmimizing -> The Bot who predicts its own next best move based on scenario of the board (win = +1)
        
        Minimizing -> Player/Extra Bot prediction of next best move based on scenario of the board (lose = -1)

        Returns a 1 when bot wins, -1 when lost, otherwise 0 when no winnable moves
        """
        if BoardGame.WinnerByRow(self.BotChr) or BoardGame.WinnerByCol(self.BotChr) or BoardGame.WinnerByDiagonal(self.BotChr): return 1
        for plr in self.Players: 
            if BoardGame.WinnerByRow(plr) or BoardGame.WinnerByCol(plr) or BoardGame.WinnerByDiagonal(plr): return -1
        if board.BoardCapacity == 0: return 0 # Whenever there is no possible win for the player or bot

        if maximizing: # We try to make the bot win in the scenario of the board
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
        else: # We try to make the player lose, likewise by predict its next move that could count a win
            bestScore: float = float("inf")

            for plr in self.Players:
                for y in range(board.BoardSize):
                    for x in range(board.BoardSize):
                        if board.isEmptySlot(x, y):
                            board.BoardData[y][x] = plr
                            board.BoardCapacity -= 1
                            score: float = self.MinMax(board, True)
                            board.BoardData[y][x] = " "
                            board.BoardCapacity += 1

                            bestScore: float = min(bestScore, score)
            return bestScore

def RenderBoard(board:Board):
    """
    Renders the whole board that is dynamic to size.
    """
    for y in range(len(board.BoardData)-1):
        print("+---"*(len(board.BoardData)-1) + "+")
        BoardRenderY: str = ""
        for x in range(len(board.BoardData[y])):
            BoardRenderY = BoardRenderY + f"| {board.BoardData[y][x]} "
        print(f"{BoardRenderY}|")
    print("+---"*(len(board.BoardData)-1) + "+")

# --- FUNCTION ---

CurrentGame = False
BotGameMode = False
PlayerTurn = 0
Robot = RobotBoard()
BoardGame = Board(3) # Create a class of 3x3 grid list, also no the bots gets recursived when the board size is >3

def play_game(Exeception = None):
    # This is usually we make a variable global so that every outside function can reach the unreachable variable
    global PlayerTurn 
    global BotGameMode, CurrentGame

    if (not CurrentGame):
        try: # basically try and catch, useful to actually not crash when inputed wrong
            b = input(f"Bot? [Y] [N]\n")
            if (b.lower() == "y" or b.lower() == "yes" or b.lower() == "ye" or b.lower() == "true" or b == 1): BotGameMode = True
            if (b.lower() == "n" or b.lower() == "no" or b.lower() == "false" or b == 0): BotGameMode = False
        except (Exception, ValueError) as e:
            print(f"Invalid? {e}")
        BoardGame.CleanBoard()

    # -- GAME FUNCTION
    CurrentGame = True
    os.system('cls' if os.name == 'nt' else 'clear')
    if (not Exeception is None): print("! Invalid Move !")
    RenderBoard(BoardGame) # Renders the board

    # PLAYER's Variable
    player: int = 0 # The Actual player
    row: int = 0
    col: int = 0
    PlayerList = ['X', 'O'] # Can be adjusted to have multiple players/bots
    Player: chr = PlayerList[PlayerTurn] # The current player
    DoNotChangeTurn: bool = False # We need to not change turn when user fails to input the numbers or bot fails prematurely
    ErrorCode = None
    
    print(f"{PlayerList}")
    print(("     "*PlayerTurn) + "  Λ  ")
    if BotGameMode and PlayerTurn != player:
        Robot.SetPlayer(PlayerList[0:PlayerTurn] + PlayerList[PlayerTurn+1:])
        Robot.SetBot(Player)
        try: # basically try and catch, useful to actually not crash when inputed wrong
            row, col = Robot.CalculateMove(BoardGame)
        except Exception as e:
            DoNotChangeTurn = True
            ErrorCode = e
    else:
        try: # basically try and catch, useful to actually not crash when inputed wrong
            row = int(input(f"Row (0 -> {BoardGame.BoardSize-1}): "))
            col = int(input(f"Column (0 -> {BoardGame.BoardSize-1}): "))
            if (row > BoardGame.BoardSize-1): raise ValueError # we can force an error
            if (col > BoardGame.BoardSize-1): raise ValueError # we can force an error
        except (Exception, ValueError) as e: # any error goes here
            DoNotChangeTurn = True
            ErrorCode = e
            

    hasWinner: bool = False
    if (not DoNotChangeTurn): 
        DoNotChangeTurn = not BoardGame.placePlayer(Player, row, col)
        if (not DoNotChangeTurn): PlayerTurn += 1
        else: ErrorCode = "no empty slot"

    # WINNER FUNCTIONALITY
    hasWinner = BoardGame.WinnerByRow(Player) or BoardGame.WinnerByCol(Player) or BoardGame.WinnerByDiagonal(Player) # Checks whether the player/bot has won
    if (hasWinner): PlayerTurn = random.randint(0, len(PlayerList)-1) # We randomize it at new game to somewhat have some turns on others
    if (PlayerTurn > len(PlayerList)-1): PlayerTurn = 0 # Reset back when >len(PlayerList) to prevent out of range error

    if (hasWinner): print(f"Player {Player} is the Winner!") # Print Winner
    elif (BoardGame.BoardCapacity <= 0): print("Tie!") # if no space and no winner print Tie
    else: play_game(ErrorCode)  # Keep going
    CurrentGame = False
    play_game()

if (__name__ == "__main__"):
    play_game()
    pass
