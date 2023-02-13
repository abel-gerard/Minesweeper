class Plot:
    def __init__(self):
        self.isOpen = False
        self.isMine = False
        self.isFlagged = False
        
        self.minefield = None # To Be Announced when in a minefield
        self.neighbors = None # To Be Announced when in a minefield
    
    def __str__(self):
        return f"Open: {self.isOpen} - Mine: {self.isMine} - Flagged: {self.isFlagged}"
    
    def __repr__(self):
        return self.__str__()
    
    def pop(self):
        '''
        0 -> Failure
        1 -> Success
        '''
        if self.isMine: return 0
        else:
            self.isOpen = True
            self.minefield.opened += 1
            if self.mineCountAround() == 0: # Recursive popping if adjacent 0-plots
                for neighbor in self.neighbors:
                    if not neighbor.isOpen: neighbor.pop()
            
            return 1
        
        # Call some internal logic for the game when a status such as this one is returned 
        
    def flag(self):
        '''
        0 -> Failure
        1 -> Success
        '''
        
        if self.isOpen: return 0
        else:
            self.isFlagged = True
            return 1
        
        # Idem
        
    def mineCountAround(self):
        if self.neighbors == None: raise AttributeError("Neighborhood not initialized.")
        return sum(map(lambda neighbor: neighbor.isMine, self.neighbors))
    
    def allOpenAround(self):
        if self.neighbors == None: raise AttributeError("Neighborhood not initialized.")
        return all(map(lambda neighbor: neighbor.isOpen, self.neighbors))