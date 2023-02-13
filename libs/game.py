from random import random
from libs.plot import*
from libs.indexToEmoji import*
from libs.app import*

class Game:
    DIFFICULTY = {
        "easy"  : ( 9,  9, 10),
        "medium": (16, 16, 40),
        "expert": (30, 16, 99)
    }
    
    def __init__(self, width, height, numberMines):
        self.width = width
        self.height = height
        self.numberMines = numberMines
        
        self.minefield = [[Plot() for _ in range(width)] for _ in range(height)]
        self.opened = 0
        
        numberPlotsRemaining = width * height
        numberMinesRemaining = self.numberMines
        
        for j in range(height): 
            for i in range(width):
                current = self.getPlot(j, i)
                current.minefield = self
                current.neighbors = self.identifyNeighbors(j, i) # For future uses
                if numberMinesRemaining == 0: 
                    continue
                
                if random() <= numberMinesRemaining / numberPlotsRemaining: 
                    current.isMine = True
                    numberMinesRemaining -= 1
                    
                numberPlotsRemaining -= 1
    
        self.app = App(self)
        self.app.run()
    
    def __str__(self):
        s = "    " + "  ".join(map(lambda num: indexToEmoji(str(num)), range(self.width))) + "\n\n"
        
        for j, row in enumerate(self.minefield):
            s += indexToEmoji(str(j)) + " "
            
            for plot in row:
                if plot.isOpen:       s += " ⬛ "
                elif plot.isFlagged:  s += " 🚩 "
                else:
                    if plot.isMine:   s += " 💣 "
                    else:             s += " ✅ "
                
            s += "\n"
        
        return s
        
    def __repr__(self):
        return self.__str__()
    
    def getPlot(self, j, i):
        return self.minefield[j][i]
    
    def identifyNeighbors(self, j, i):
        return [self.getPlot(y, x) for x in range(i - 1, i + 2) 
                                   for y in range(j - 1, j + 2) 
                                   if (y, x) != (j, i)     and
                                      0 <= y < self.height and
                                      0 <= x < self.width      ]
        