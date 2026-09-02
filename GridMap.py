##########################
#                        #
#  Whole Class Grid Map  #
# VSTUDIOS & VvSeanGtvV  #
#         2026           #
#                        #
##########################

class Vector2:
    x: int
    y: int
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

class Map:
    MapSize = 0
    MapData = [[]]
    def __init__(self, size):
        self.MapSize = size
        for y in range(0, size):
            self.MapData.append([])
            for x in range(0, size):
                if y <= 0 or y >= size - 1 or x <= 0 or x >= size - 1:
                    self.MapData[y].append(1)
                else:
                    self.MapData[y].append(0)
    
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
                if data[y][x] == 2:
                    bData = bData + "P"
                elif data[y][x] == 1:
                    bData = bData + "#"
                else:
                    bData = bData + " "
            print(bData)

class Player:
    Data: Map
    Position: Vector2
    def __init__(self, Data: Map):
        self.Data = Data
        self.Position = Vector2(Data.MapSize//2, Data.MapSize//2)

    def move(self, H, V):
        isCollidable = self.Data.GetTileMap(self.Position.x + V, self.Position.y + H) == 1
        if not isCollidable:
            Data.SetTileMap(Plr.Position.x, Plr.Position.y, 0)
            self.Position.x += V
            self.Position.y += H

    
Data = Map(25)
Render = Renderer(Data)
Plr = Player(Data)

while True:
    Data.SetTileMap(Plr.Position.x, Plr.Position.y, 2)
    Render.render()

    wasdMap = ["w", "a", "s", "d"]
    control = input("W A S D \n").lower()
    for i in range(0, len(control)):
        if control[i] == "w":
            Plr.move(-1, 0)
        if control[i] == "s":
            Plr.move(1, 0)
        if control[i] == "a":
            Plr.move(0, -1)
        if control[i] == "d":
            Plr.move(0, 1)


