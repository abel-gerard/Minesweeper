import pygame as pg
from os import system

class App:
    PLOT_COLOR = (15, 245, 76)
    
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
    
    def __init__(self, caller):
        pg.init
        pg.display.set_caption("Minesweeper")
        
        self.caller = caller
        
        self.screen = pg.display.set_mode(self.defineSurfaceSize())
        self.surfaceSize = self.defineSurfaceSize()
        self.running = False
    
    def defineSurfaceSize(self):
        return (App.OFFSET_FROM_SIDE["left"] + App.OFFSET_FROM_SIDE["right"] + 
                self.caller.width  * (App.PLOT_DIMENSION["x"] + App.PLOT_DIMENSION["horizontalSpacing"]) - App.PLOT_DIMENSION["horizontalSpacing"],
                App.OFFSET_FROM_SIDE["top" ] + App.OFFSET_FROM_SIDE["down" ] + 
                self.caller.height * (App.PLOT_DIMENSION["y"] + App.PLOT_DIMENSION["verticalSpacing"  ]) - App.PLOT_DIMENSION["verticalSpacing"  ])
    
    def showToConsole(self):
        system("cls")
        print(self.caller)
    
    def mousePositionToCoordinate(self, position):
        y = (position[1] - App.OFFSET_FROM_SIDE["top" ]) // (App.PLOT_DIMENSION["y"] + App.PLOT_DIMENSION["verticalSpacing"  ])
        x = (position[0] - App.OFFSET_FROM_SIDE["left"]) // (App.PLOT_DIMENSION["x"] + App.PLOT_DIMENSION["horizontalSpacing"])
        
        return (y, x)
    
    def run(self):
        self.running = True
        ### Debug view
        self.showToConsole()
        ###
        while self.running:
            LMB, RMB = False, False

            for evt in pg.event.get():
                if evt.type == pg.QUIT:
                    self.running = False
                    
                elif evt.type == pg.MOUSEBUTTONDOWN:
                    if   pg.mouse.get_pressed() == (1, 0, 0): # Detects left click
                        LMB = True

                    elif pg.mouse.get_pressed() == (0, 0, 1): # Right click
                        RMB = True
                        
                    mousePos = pg.mouse.get_pos()
                    coord = self.mousePositionToCoordinate(mousePos)
                    if self.caller.getPlot(*coord).pop() == 0: 
                        # print("Game Over!")
                        self.running = False
                        
                    ### Debug view 
                    self.showToConsole()
                    ###
            
            pg.display.flip()
        