import os
import random

##########################
#                        #
#    Whole Game Grid     #
# VSTUDIOS & VvSeanGtvV  #
#     09 / 14 / 2026     #
#                        #
##########################


## PYTHON CLASS
class Vector2:
    x: int
    y: int
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

class TileMap:
    Map = [
        "#", #WALL
        "P", #PLAYER
        " ", #SPACE
        "T" #TREE
    ]
    def __init__(self):
        pass

class Map:
    MapSize = 0
    MapData = [[]]
    TileMapData: TileMap = TileMap()
    def __init__(self, size: int):
        self.MapSize = size
        for y in range(0, size):
            self.MapData.append([])
            for x in range(0, size):
                if y <= 0 or y >= size - 1 or x <= 0 or x >= size - 1:
                    self.MapData[y].append(0)
                else:
                    self.MapData[y].append(random.randint(2,3)) 
    
    def SetTileMap(self, x: int, y: int, data: int):
        self.MapData[y][x] = data
    
    def GetTileMap(self, x: int, y: int):
        return self.MapData[y][x]

class Renderer:
    MapData: Map = NotImplemented
    def __init__(self, map: Map):
        self.MapData = map

    def render(self):
        data = self.MapData.MapData
        size = self.MapData.MapSize
        for y in range(0, size):
            bData: str = ""
            for x in range(0, size):
                bData = bData + self.MapData.TileMapData.Map[data[y][x]]
            print(bData)

class Player:
    Standing: int = 2
    Data: Map = NotImplemented
    Position: Vector2 = Vector2()
    Inventory = [0, 0, 0]
    def __init__(self, Data: Map):
        self.Data = Data
        self.Position = Vector2(Data.MapSize//2, Data.MapSize//2)

    def move(self, H, V):
        isCollidable = self.Data.GetTileMap(self.Position.x + V, self.Position.y + H) == 0
        if not isCollidable:
            Data.SetTileMap(Plr.Position.x, Plr.Position.y, self.Standing)
            self.Standing = self.Data.GetTileMap(self.Position.x + V, self.Position.y + H)
            self.Position.x += V
            self.Position.y += H
    
    def mine(self):
        self.Inventory[self.Standing - 3] += 1
        self.Standing = 2


## MAIN FUNCTION
Data = Map(32)
Render = Renderer(Data)
Plr = Player(Data)

def UIPrint(IN: str, Length:int):
    UIS:str = IN
    BarLength: int=Length-2
    print("#"+UIS+(" "*(BarLength-len(UIS))+"#")) 

def UI():
    BarSize: int = 18
    print("#"*18)
    UIPrint(" Standing on: " + Data.TileMapData.Map[Plr.Standing], BarSize)
    UIPrint(f" Logs : {Plr.Inventory[0]} ", BarSize)
    UIPrint(f" Stone : {Plr.Inventory[1]} ", BarSize)
    UIPrint(f" Ores : {Plr.Inventory[2]} ", BarSize)
    print("#"*18)

while True:
    # Clears the screen dynamically across all major systems
    os.system('cls' if os.name == 'nt' else 'clear')
    Data.SetTileMap(Plr.Position.x, Plr.Position.y, 1)
    Render.render()
    UI()

    wasdMap = ["w", "a", "s", "d", "m"]
    controlUI = "W A S D"
    if (Plr.Standing > 2): controlUI += " M"
    control = input(controlUI+"\n").lower()
    for i in range(0, len(control)):
        if control[i] == "w":
            Plr.move(-1, 0)
        if control[i] == "s":
            Plr.move(1, 0)
        if control[i] == "a":
            Plr.move(0, -1)
        if control[i] == "d":
            Plr.move(0, 1)
        if (control[i] == "m" and Plr.Standing > 2):
            Plr.mine()
