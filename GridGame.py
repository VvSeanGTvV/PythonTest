import os
import random

##########################
#                        #
#    Whole Game Grid     #
# VSTUDIOS & VvSeanGtvV  #
#     09 / 14 / 2026     #
#                        #
##########################

# CHANGELOG
# 09 / 16 / 2026 - Color Update lol


## PYTHON CLASS
class Vector2:
    x: int
    y: int
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

class TileMap:
    Map = [
        "\033[1;37;47m ", #WALL
        "\033[1;33;43m ", #PLAYER
        "\033[1;30;40m ", #SPACE
        "\033[1;32;40mT", #TREE
        "\033[1;31;40mS", #STONE
        "\033[1;36;40mO" #ORE
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
            z: int = random.randint(0, 2)
            self.MapData.append([])
            for x in range(0, size):
                if y <= 0 or y >= size - 1 or x <= 0 or x >= size - 1:
                    self.MapData[y].append(0)
                else:
                    self.MapData[y].append(random.randint(2,3+z)) 
    
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
                bData = bData + self.MapData.TileMapData.Map[data[y][x]] + "\033[1;37;40m"
            print(bData)

class Player:
    Standing: int = 2
    Data: Map = NotImplemented
    Position: Vector2 = Vector2()
    Inventory = [0, 0, 0, 0]
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
        ItemType: int = self.Standing - 3
        if (ItemType == 0): self.Inventory[ItemType] += random.randint(0, 3)
        self.Inventory[ItemType] += 1
        self.Standing = 2


## MAIN FUNCTION
build = "09162026"
Data = Map(32)
Render = Renderer(Data)
Plr = Player(Data)

def UIPrint(IN: str, Length:int, Offset:int = 1):
    UIS:str = IN
    BarLength: int = (Length * Offset) - 4
    print("\033[1;37;47m "+UIS+("\033[0m "*(BarLength-len(UIS))+"\033[1;37;47m \033[1;37;40m")) 

def UI():
    BarSize: int = 32
    print("\033[1;30;40m")
    print("\033[1;37;47m "*BarSize + "\033[1;37;40m")
    UIPrint(f"\033[1;33;40m Pyt\033[1;36;40mhon\033[1;37;40m Grid Game | {build} \033[1;37;40m ", BarSize)
    UIPrint(f"\033[1;37;40m Standing on: {Data.TileMapData.Map[Plr.Standing]}\033[1;37;40m", BarSize, 2)
    UIPrint(f"\033[1;32;40m Log\033[1;37;40m  | x{Plr.Inventory[0]}\033[1;37;40m", BarSize, 2)
    UIPrint(f"\033[1;36;40m Ore\033[1;37;40m  | x{Plr.Inventory[2]}\033[1;37;40m", BarSize, 2)
    UIPrint(f"\033[1;31;40m Stone\033[1;37;40m  | x{Plr.Inventory[1]}\033[1;37;40m", BarSize, 2)
    UIPrint(f"\033[1;34;40m Ingot\033[1;37;40m  | x{Plr.Inventory[3]}\033[1;37;40m", BarSize, 2)
    print("\033[1;37;47m "*BarSize + "\033[1;37;40m")

def main():
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

main()
