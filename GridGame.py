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
# 09 / 21 / 2026 - Crafting W.I.P.
# 09 / 23 / 2026 - Crafting W.I.P. (test 1) + Mining Tier

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
        "\033[1;36;40mO", #ORE
        "\033[1;32;40mW", #TREE
        "\033[1;32;40mC", #WORKBENCH
        "\033[1;31;40mF", #FURNACE
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
            for x in range(0, size*3):
                if y <= 0 or y >= size - 1 or x <= 0 or x >= size*3 - 1:
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
            for x in range(0, size*3):
                bData = bData + self.MapData.TileMapData.Map[data[y][x]] + "\033[1;37;40m"
            print(bData)

class Player:
    Standing: int = 2
    Data: Map = NotImplemented
    Position: Vector2 = Vector2()
    Inventory = [0, 0, 0, 0, 0, 0] #Log, Stone, Ore, Ingot, Workbench, Furnace
    MineTier: int = 0

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
        if (ItemType == 1 and self.MineTier <= 0): return
        if (ItemType == 2 and self.MineTier <= 1): return
        self.Inventory[ItemType] += 1
        self.Standing = 2
    
    def place(self, id:int):
        ItemType: int = id
        if (ItemType >= 4):
            LeftBlocks: int = self.Inventory[id]
            if (LeftBlocks > 0):
                if (self.Standing - 3 >= 0): self.mine()
                self.Inventory[id] -= 1
                self.Standing = id + 3
    
    def craft(self, id:int):
        if (id == 4 and self.Inventory[0] >= 4):
            self.Inventory[0] -= 4
            self.Inventory[4] += 1
        if (id == 5 and self.Inventory[1] >= 8):
            self.Inventory[1] -= 8
            self.Inventory[5] += 1
        if (id == 3 and self.Inventory[2] >= 1):
            self.Inventory[2] -= 1
            self.Inventory[3] += 1
        if (id == 10 and self.Inventory[0] >= 9 and self.MineTier == 0):
            self.Inventory[0] -= 9
            self.MineTier += 1
        if (id == 11 and self.Inventory[1] >= 9 and self.MineTier == 1):
            self.Inventory[1] -= 9
            self.MineTier += 1

## MAIN FUNCTION
build = "09232026"
Data = Map(32)
Render = Renderer(Data)
Plr = Player(Data)
UIArea: int = 0

def UIPrint(IN: str, Length:int, Offset:int = 1):
    UIS:str = IN
    BarLength: int = (Length * Offset) - 4
    print("\033[1;37;47m "+UIS+("\033[0m "*(BarLength-len(UIS))+"\033[1;37;47m \033[1;37;40m")) 

def UI(UI:int = 0):
    BarSize: int = 32

    print("\033[1;30;40m")
    if (UI == 0 or UI >= 0):
        print("\033[1;37;47m "*BarSize + "\033[1;37;40m")
        UIPrint(f"\033[1;33;40m Pyt\033[1;36;40mhon\033[1;37;40m Grid Game | {build} \033[1;37;40m ", BarSize)
        UIPrint(f"\033[1;37;40m Standing on: {Data.TileMapData.Map[Plr.Standing]}\033[1;37;40m", BarSize, 2)
        UIPrint(f"\033[1;3{Plr.MineTier+2};40m Mining\033[1;37;40m Tier: {Plr.MineTier}\033[1;37;40m", BarSize, 2)
        UIPrint(f"\033[1;32;40m Log\033[1;37;40m | x{Plr.Inventory[0]}\033[1;37;40m", BarSize, 2)
        UIPrint(f"\033[1;36;40m Ore\033[1;37;40m | x{Plr.Inventory[2]}\033[1;37;40m", BarSize, 2)
        UIPrint(f"\033[1;31;40m Stone\033[1;37;40m | x{Plr.Inventory[1]}\033[1;37;40m", BarSize, 2)
        UIPrint(f"\033[1;34;40m Ingot\033[1;37;40m | x{Plr.Inventory[3]}\033[1;37;40m", BarSize, 2)
        
    if (UI == 4):
        print("\033[1;37;47m "*BarSize + "\033[1;37;40m")
        UIPrint(f"\033[1;37;40m     Placing      Station   \033[1;37;40m \033[1;37;40m ", BarSize)
        UIPrint(f"\033[1;32;40m Workbench\033[1;37;40m | x{Plr.Inventory[4]} [1] \033[1;37;40m", BarSize, 2)
        UIPrint(f"\033[1;31;40m Furnace\033[1;37;40m | x{Plr.Inventory[5]} [2] \033[1;37;40m", BarSize, 2)

    if (UI == 1 or UI == 2 or UI == 3):
        print("\033[1;37;47m "*BarSize + "\033[1;37;40m")
        if (UI == 1 or UI == 2): UIPrint(f"\033[1;37;40m     Crafting     Station   \033[1;37;40m \033[1;37;40m ", BarSize)
        if (UI == 3): UIPrint(f"\033[1;37;40m     Furnace      Station   \033[1;37;40m \033[1;37;40m ", BarSize)
        if (UI == 1):
            UIPrint(f"\033[1;32;40m x4 Logs -> Workbench\033[1;37;40m [1] x{Plr.Inventory[4]} \033[1;37;40m", BarSize, 2)
        if (UI == 2):
            UIPrint(f"\033[1;31;40m x8 Stone -> Furnace\033[1;37;40m [1] x{Plr.Inventory[5]} \033[1;37;40m", BarSize, 2)
            UIPrint(f"\033[1;32;40m x9 Logs -> Mine Tier 1\033[1;37;40m [2] \033[1;37;40m", BarSize, 2)
            UIPrint(f"\033[1;31;40m x9 Stone -> Mine Tier 2\033[1;37;40m [3] \033[1;37;40m", BarSize, 2)
        if (UI == 3):
            UIPrint(f"\033[1;34;40m x1 Ore -> Ingot\033[1;37;40m [1] x{Plr.Inventory[3]} \033[1;37;40m", BarSize, 2)
    print("\033[1;37;47m "*BarSize + "\033[1;37;40m")

def main():
    # GLOBAL
    global UIArea

    while True:
        # Clears the screen dynamically across all major systems
        os.system('cls' if os.name == 'nt' else 'clear')
        Data.SetTileMap(Plr.Position.x, Plr.Position.y, 1)
        Render.render()
        if (UIArea <= 0): UI()
        if (UIArea > 0): UI(UIArea)

        controlUI = "W A S D C I"
        if (Plr.Standing > 2): controlUI += " M"
        if (UIArea == 1): controlUI = "C 1 2 3"
        if (UIArea == 4): controlUI = "I 1 2"
        control = input(controlUI+"\n").lower()
        for i in range(0, len(control)):
            if (UIArea <= 0):
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
            if (UIArea == 1):
                if control[i] == "1":
                    Plr.craft(4)
            if (UIArea == 2):
                if control[i] == "1":
                    Plr.craft(5)
                if control[i] == "2":
                    Plr.craft(10)
                if control[i] == "3":
                    Plr.craft(11)
            if (UIArea == 3):
                if control[i] == "1":
                    Plr.craft(3)
            if (UIArea == 4):
                if control[i] == "1":
                    Plr.place(4)
                if control[i] == "2":
                    Plr.place(5)
            if control[i] == "c":
                if (UIArea <= 0 and Plr.Standing == 8): UIArea = 3
                elif (UIArea <= 0 and Plr.Standing == 7): UIArea = 2
                elif (UIArea <= 0): UIArea = 1
                elif (UIArea > 0): UIArea = 0
            if control[i] == "i":
                if (UIArea <= 0): UIArea = 4
                elif (UIArea > 0): UIArea = 0

main()
