import pygame as pg
from os import system

class App:
    COLOR = {
        "plot"       : ( 15, 245,  76),
        "poppedPlot" : (  0,   0,   0),
        "flaggedPlot": (255,   0,   0)
    }
    
    OFFSET_FROM_SIDE = {
            "top": 20,
            "right": 20,
            "down": 20,
            "left": 20
        }
        
    PLOT_DIMENSION = {
        "x": 50,
        "y": 50,
        "horizontalSpacing": 10,
        "verticalSpacing": 10
    }
    
    pg.font.init()
    FONT = pg.font.Font('freesansbold.ttf', int(min(PLOT_DIMENSION["x"], PLOT_DIMENSION["y"]) * (16 / 25)))
    
    def __init__(self, caller):
        pg.init
        pg.display.set_caption("Minesweeper")
        
        self.caller = caller
        
        self.displaySize = self.defineDisplaySize()
        self.screen = pg.display.set_mode(self.displaySize)        
        self.running = False
    
    def defineDisplaySize(self):
        return (App.OFFSET_FROM_SIDE["left"] + App.OFFSET_FROM_SIDE["right"] + 
                self.caller.width  * (App.PLOT_DIMENSION["x"] + App.PLOT_DIMENSION["horizontalSpacing"]) - App.PLOT_DIMENSION["horizontalSpacing"],
                App.OFFSET_FROM_SIDE["top" ] + App.OFFSET_FROM_SIDE["down" ] + 
                self.caller.height * (App.PLOT_DIMENSION["y"] + App.PLOT_DIMENSION["verticalSpacing"  ]) - App.PLOT_DIMENSION["verticalSpacing"  ])
    
    def showToConsole(self):
        system("cls")
        print(self.caller)
    
    def mousePositionToCoordinates(self, position):
        j = (position[0] - App.OFFSET_FROM_SIDE["top" ]) // (App.PLOT_DIMENSION["y"] + App.PLOT_DIMENSION["verticalSpacing"  ])
        i = (position[1] - App.OFFSET_FROM_SIDE["left"]) // (App.PLOT_DIMENSION["x"] + App.PLOT_DIMENSION["horizontalSpacing"])
        
        return (j, i)
    
    def coordinatesToPosition(self, coordinates):
        y = coordinates[0] * (App.PLOT_DIMENSION["y"] + App.PLOT_DIMENSION["verticalSpacing"  ]) + App.OFFSET_FROM_SIDE["top" ]
        x = coordinates[1] * (App.PLOT_DIMENSION["x"] + App.PLOT_DIMENSION["horizontalSpacing"]) + App.OFFSET_FROM_SIDE["left"]
        
        return (y, x)
    
    def drawPlot(self, position, color):
        pg.draw.rect(self.screen, 
                     color, 
                     pg.Rect(position[1], position[0], App.PLOT_DIMENSION["x"], App.PLOT_DIMENSION["y"]),
                     border_radius=5)
    
    def run(self):
        self.running = True
        ### Debug view
        # self.showToConsole()
        ###
        
        while self.running:
            if self.caller.opened == self.caller.width * self.caller.height - self.caller.numberMines:
                self.running = False
            
            LMB, RMB = False, False
            for j in range(self.caller.height):
                for i in range(self.caller.width):
                    position = self.coordinatesToPosition((j, i))
                    current = self.caller.getPlot(j, i)
                    
                    if current.isFlagged and not current.isOpen:
                        color = App.COLOR["flaggedPlot"]
                    else:
                        if current.isOpen:
                            color = App.COLOR["poppedPlot"]
                        else:
                            color = App.COLOR["plot"]
                        
                    self.drawPlot(position, color)
                    
                    if not current.allOpenAround() and current.isOpen:
                        text = App.FONT.render(str(current.mineCountAround()), True, App.COLOR["plot"], App.COLOR["poppedPlot"])
                        textZone = text.get_rect()
                        textZone.center = position[1] + App.PLOT_DIMENSION["x"] // 2, position[0] + App.PLOT_DIMENSION["y"] // 2
                        self.screen.blit(text, textZone)
                    # print(textZone.center)
            
            for evt in pg.event.get():
                if evt.type == pg.QUIT:
                    self.running = False
                    
                elif evt.type == pg.MOUSEBUTTONDOWN:
                    if   pg.mouse.get_pressed() == (1, 0, 0): # Detects left click
                        LMB = True

                    elif pg.mouse.get_pressed() == (0, 0, 1): # Right click
                        RMB = True
                        
                    mousePos = pg.mouse.get_pos()
                    coord = self.mousePositionToCoordinates(mousePos[::-1])
                    current = self.caller.getPlot(*coord)
                    if LMB and not current.isFlagged:
                        if current.pop() == 0: 
                            # print("Game Over!")
                            self.running = False
                        
                    elif RMB:
                        current.isFlagged = not current.isFlagged
                        
                    ### Debug view 
                    # self.showToConsole()
                    ###
            
            pg.display.flip()
        