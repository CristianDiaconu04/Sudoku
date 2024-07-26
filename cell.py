class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num = 0
        self.clickable = False
        self.square = (x // 3) * 3 + (y // 3)
        self.original = False 
